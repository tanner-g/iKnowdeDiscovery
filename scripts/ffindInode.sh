#!/bin/bash

partition=$1
entry=$2
result="$(sudo ffind $partition $entry)"
echo "  $entry -> $result" >> report.txt
