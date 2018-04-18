import pygeoip
import plotly
import json
import plotly.figure_factory as figure
from plotly.graph_objs import *
import networkx as nx
import matplotlib.pyplot as plt

def load_json():
    """Loads json data from "final.json". This data is then returned to
        visualize() for use in Plotly visuals.
    """
    with open('final.json', 'r') as input_file:
        data = json.load(input_file)
    return data

def get_ips(jsondata):
    """Uses the IPFlow data from the jsondata to gather IPs found in the traffic
        and performs a reverse lookup to find the origin country. The country is
        then added to a hashmap and the occurrences are recorded for a bar graph.
        Graph_geoIP() is then called and passed the observed countries in the
        x_axis and the occurrences as the y_axis.

        jsondata - The loaded data as parsed by parse.py containing statistics
            and information for graphing visuals.
    """
    geo_lookup = pygeoip.GeoIP('GeoIP.dat')
    ips = jsondata['Statistics']['IPflow']
    ip_mapping = dict()
    mapping_occurrence = dict()

    for ip in ips:
        source, dest = ip.split(' ')
        source_country = geo_lookup.country_name_by_addr(source)
        dest_country = geo_lookup.country_name_by_addr(dest)
        if source_country in mapping_occurrence.keys():
            mapping_occurrence[source_country] += 1
        else:
            mapping_occurrence[source_country] = 1
        if dest_country in mapping_occurrence.keys():
            mapping_occurrence[dest_country] += 1
        else:
            mapping_occurrence[dest_country] = 1
    country_x_axis = list()
    country_y_axis = list()
    for key in mapping_occurrence.keys():
        country_x_axis.append(key)
        country_y_axis.append(mapping_occurrence[key])
    graph_geoIP(country_x_axis, country_y_axis)


def graph_geoIP(x_axis, y_axis):
    """Creates a bar graph with Plotly showing geoIP locations of the traffic
        observed in the Snort alerts and how many times that country is
        observed in the traffic.
        The x_axis contains the countries observed and the y_axis shows the
        number of occurrences.
        The resulting HTML from Plotly is written in the templates folder in
        "geoIP_bar.html" which the Flask app can use.

        x_axis - A list of countries observed in the Snort alert traffic.
        y_axis - A list of the occurrences of each country in the list.
    """
    data = [plotly.graph_objs.Bar(
            x=x_axis,
            y=y_axis
    )]
    embed = plotly.offline.plot(data, show_link=False, output_type='div', auto_open=False)
    f = open('templates/geoIP_bar.html', 'w')
    f.write(embed)
    f.close()

def top_alerts(jsondata):
    """Uses the 'Message' field in jsondata to record the occurrences of each
        Snort alert. Every message is added to a hashmap and the occurences of
        each message is recorded. The hashmap is then converted into a list
        with the format of ['Message', 'Occurrences']. The list is then sorted
        with sort_lists(), and shortened to the top ten messages. The shortened
        list is then sent to plot_message_table() to be graphed with Plotly.

        jsondata - The loaded data as parsed by parse.py containing statistics
            and information for graphing visuals.
    """
    alerts = jsondata['Values']
    alert_map = dict()
    alert_list = list()
    for alert in alerts:
        message = alert['Message']
        if message in alert_map.keys():
            alert_map[message] += 1
        else:
            alert_map[message] = 1
    for key in alert_map.keys():
        item = [key, alert_map[key]]
        alert_list.append(item)
    sorted_list = sort_lists(alert_list)
    build_table('Messages', sorted_list, 'templates/message_table.html')

def sort_lists(list_to_sort):
    """Custom sorting function that will sort a list and will truncate the list
        to save only the top ten items. Returns sorted_list, a list of size 10
        or smaller.

        list_to_sort - The passed list that needs sorting.
    """
    sorted_list = list()
    while len(list_to_sort) != 0:
        curr = list_to_sort[0]
        for item in list_to_sort:
            if item[1] > curr[1]:
                curr = item
        list_to_sort.remove(curr)
        sorted_list.append(curr)
    if len(sorted_list) > 10:
        sorted_list = sorted_list[:10]
    return sorted_list

def port_tables(jsondata):
    """Parses the PortFlow statistics provided by jsondata and creates two
        lists for creation of the most common source ports and most common
        destination ports. The source and destination ports and their
        occurrences are recording in hashmaps that are converted to lists. These
        lists are then sorted with sort_lists() and truncated to the top ten
        ports.
        Build_table() is then called twice to build a source port table and a
        destination port table. These table can be found in the templates folder
        named "source_table.html" and "dest_table.html".

        jsondata - The loaded data as parsed by parse.py containing statistics
            and information for graphing visuals.
    """
    portFlow = jsondata['Statistics']['Portflow']
    source_dict = dict()
    dest_dict = dict()
    source_list = list()
    dest_list = list()

    for entry in portFlow:
        flow = entry.split(' ')
        if flow[0] in source_dict.keys():
            source_dict[flow[0]] += portFlow[entry]
        else:
            source_dict[flow[0]] = portFlow[entry]
        if flow[1] in dest_dict.keys():
            dest_dict[flow[1]] += portFlow[entry]
        else:
            dest_dict[flow[1]] = portFlow[entry]

    for key in source_dict.keys():
        item = [key, source_dict[key]]
        source_list.append(item)

    for key in dest_dict.keys():
        item = [key, dest_dict[key]]
        dest_list.append(item)

    sorted_source_list = sort_lists(source_list)
    sorted_dest_list = sort_lists(dest_list)
    build_table('Source Port', sorted_source_list, 'templates/source_table.html')
    build_table('Destination Port', sorted_dest_list, 'templates/dest_table.html')

def build_table(table_type, list_to_use, filename):
    """Builds a generic table for Plotly visualizations. Given the information
        provided to the function, it will insert table headers at the beginning
        of the sorted list and that list will be passed to plotly for table
        generation. The Plotly output in HTML format will then be written to the
        specified file in the templates folder for the Flask app to use.

        table_type - The type of table to be generated, determined the first
            table header.
        list_to_use - The sorted list of information to push up to Plotly.
        filename - The path/name of the file that Plotly HTMl output should be
            saved to.
    """
    list_to_use.insert(0, [table_type, 'Occurences'])
    table = figure.create_table(list_to_use)
    embed = plotly.offline.plot(table, show_link=False, output_type='div', auto_open=False)
    f = open(filename, 'w')
    f.write(embed)
    f.close()

#here
#here
#HERE
def network_graph(jsondata):
    """Creates a force-directed network graph using the IPFlow information
        provided by the 'Statistics' key in jsondata. This graph shows the
        nodes in the network and how they connect to each other through Snort
        alerts. There is also a color gradient where the color reflects the
        number of connections a specific node is involved in. The IPFlow
        information is parsed and pushed to Plotly and the resulting HTML is
        saved in the templates folder in "network.html" for use of the Flask
        app.

        jsondata - The loaded data as parsed by parse.py containing statistics
            and information for graphing visuals.
    """
    ips = jsondata['Statistics']['IPflow']
    nodes = set()
    connections = set()
    for item in ips:
        separate_ips = item.split(' ')
        nodes.add(separate_ips[0])
        nodes.add(separate_ips[1])
        make_tuple = (separate_ips[0], separate_ips[1]);
        connections.add(make_tuple)

    G = nx.Graph()
    Nodes = nodes
    G.add_nodes_from(Nodes)
    Edges = connections
    G.add_edges_from(Edges)
    pos = nx.spring_layout(G)

    edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=Marker(
            showscale=True,
            colorscale='Bluered',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                xanchor='left',
                title='Connections',
                titleside='right'
            ),
            line=dict(width=2)))

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    for node in G.nodes():
        weight = 0
        for edge in G.edges():
            if node == edge[0] or node == edge[1]:
                flow = edge[0] + " " + edge[1]
                flow2 = edge[1] + " " + edge[0]
                try:
                    weight += jsondata['Statistics']['IPflow'][flow]
                except:
                    weight += 0
                try:
                    weight += jsondata['Statistics']['IPflow'][flow2]
                except:
                    weight += 0
        node_trace['marker']['color'].append(weight)
        node_info = '# of connections: '+str(weight) + '\n' + str(node)
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
            layout=Layout(
            titlefont=dict(size=16),
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            annotations=[ dict(
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002 ) ],
            xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    embed = plotly.offline.plot(fig, show_link=False, output_type='div', auto_open=False)
    f = open('templates/network.html', 'w')
    f.write(embed)
    f.close()

def plot_priority(jsondata):
    """Uses to priorities statistics in jsondata to create a Plotly pie chart
        showing the occurrences of each priority level alert in Snort. There are
        five alert levels ranging from 1 (not serious) to 5 (critical). Passing
        in the priority levels to Plotly as well as the occurrences of each
        level allow for the user to see if there is a surge of certain priority
        alerts. The HTML generated by Plotly is saved in the templates folder
        in "priority.html". 

        jsondata - The loaded data as parsed by parse.py containing statistics
            and information for graphing visuals.
    """
    item = jsondata['Statistics']['Priorities']
    prioritylist = list()
    prioritylevellist = list()
    for thing in item:
        prioritylist.append(thing)
        prioritylevellist.append(item[thing])
    trace1 = {
        "domain": {
            "x": [0, 1],
            "y": [0, 1]
        },
        "hoverinfo": "all",
        "labels": prioritylist,
        "marker": {"colors": ["#7fc97f", "#beaed4", "#fdc086", "#ffff99", "#386cb0"]},
        "name": "Value",
        "pull": 0,
        "showlegend": True,
        "textinfo": "value",
        "type": "pie",
        "uid": "f4de1f",
        "values": prioritylevellist
    }
    data = Data([trace1])
    layout = {
        "autosize": False,
        "height": 500,
        "width": 800
    }
    fig = Figure(data=data, layout=layout)
    embed = plotly.offline.plot(fig, show_link=False, output_type='div', auto_open=False)
    f = open('templates/priority.html', 'w')
    f.write(embed)
    f.close()

def plot_protocol(jsondata):
    """Creates a pie chart displaying the occurrences of TCp vs. UDP traffic. It
        uses jsondata's protocol statistics and passes to Plotly the list of
        protocols [TCP, UDP] and then passes Plotly a list of each protocol's
        occurrences for recording on the pie chart. The HTML generated by Plotly
        is saved in the templates folder as "protocol.html".
        Current dashboard implementation does not use this visual, but future
        plans of custom dashboards warrant keeping this function.

        jsondata - The loaded data as parsed by parse.py containing statistics
            and information for graphing visuals.
    """
    item = jsondata['Statistics']['Protocol']
    protocol_list = list()
    protocol_occurences = list()
    for thing in item:
        protocol_list.append(thing)
        protocol_occurences.append(item[thing])
    trace1 = {
        "domain": {
            "x": [0, 1],
            "y": [0, 1]
        },
        "hoverinfo": "all",
        "labels": protocol_list,
        "marker": {"colors": ["#ffff99", "#386cb0", "#7fc97f", "#beaed4", "#fdc086"]},
        "name": "Value",
        "pull": 0,
        "showlegend": True,
        "textinfo": "value",
        "type": "pie",
        "uid": "f4de1f",
        "values": protocol_occurences
    }
    data = Data([trace1])
    layout = {
        "autosize": False,
        "height": 500,
        "width": 800
    }
    fig = Figure(data=data, layout=layout)
    embed = plotly.offline.plot(fig, show_link=False, output_type='div', auto_open=False)
    f = open('templates/protocol.html', 'w')
    f.write(embed)
    f.close()

def visualize():
    """Primary function that causes the visual processing and generation to occur.
        Will be called from the Flask app upon start.
    """
    jsondata = load_json()
    plot_protocol(jsondata)
    plot_priority(jsondata)
    network_graph(jsondata)
    top_alerts(jsondata)
    port_tables(jsondata)
    get_ips(jsondata)

if __name__ == "__main__":
    visualize()
