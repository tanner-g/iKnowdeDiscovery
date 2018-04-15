#!/bin/bash
partition=/dev/mapper/fedora-root

iter=100

while [ $iter -le 110 ]
do
sudo istat $partition $iter >> res.txt
((iter++))
done
