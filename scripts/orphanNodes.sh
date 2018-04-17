#!/bin/bash
partition=/dev/mapper/fedora-root
fsstat $partition > /usr/tmp/iKnowdeDiscovery/fsstat.txt
python fsstat.py
