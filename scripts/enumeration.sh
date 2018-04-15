#!/bin/bash

declare search_dir="/home/user/Desktop/testy"

echo "Using Directory: $search_dir"

use_dir=$search_dir
use_dir+="/*"
tmp_dir=$search_dir
tmp_dir+="/enum_tmp"

fileNames=($use_dir)
declare -a inodes=()
declare -A files=()
#declare -A animals=( ["moo"]="cow" ["woof"]="dog")
count=${#fileNames[@]}

mkdir -p $tmp_dir;

for ((i=0; i<$count; i++)); do
	printf "%s\n" "${fileNames[$i]}" > "$tmp_dir/$i.txt"
	printf "%s\n" "$(ls -i ${fileNames[$i]} | awk '{print $1}')" >> "$tmp_dir/$i.txt"
done

for ((i=0; i<$count; i++)); do
	
done

chmod -R 777 $tmp_dir;

if [ -d $tmp_dir ]; then
	rm -rf $tmp_dir;
fi
