import plotly
from plotly.graph_objs import *
import networkx as nx
import matplotlib.pyplot as plt
import os

path = "/usr/tmp/iKnowdeDiscovery/enum/"

dictionaries = list()

for data_file in os.listdir(path):
    with open(os.path.join(path,data_file)) as file_pp:
        file_dict = list()
        first_line = True
        files = []
        inode = 0
        for line in file_pp:
            if first_line:
                first_line = False
            else:
                if line:
                    tmp = line.strip("\n").split("\t")
                    files.append(tmp[1])
                    if inode == 0:
                        inode = tmp[0]
        dictionaries.append([inode, files])
        inode = 0
        files = []
        file_dict = list()
nodes = set()
connections = set()
weights = dict()
for inodes in dictionaries:
    nodes.add(str(inodes[0]))
    weights[str(inodes[0])] = len(inodes[1])
    for item in inodes[1]:
        nodes.add(str(item))
        weights[str(item)] = len(inodes[1])
        make_tuple = (inodes[0], item);
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
    node_trace['marker']['color'].append(weights[str(node)])
    node_info = '# of connections: '+str(weights[str(node)]) + '\n' + str(node)
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
f = open('inode.html', 'w')
f.write(embed)
f.close()

