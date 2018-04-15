#!/bin/bash
partition=/dev/mapper/fedora-root

fsstat $partition > fsstat.txt
python fsstat.py
