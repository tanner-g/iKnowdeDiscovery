#!/bin/bash
partition=$1
fsstat $partition > /usr/tmp/iKnowdeDiscovery/fsstat.txt
python fsstat.py
