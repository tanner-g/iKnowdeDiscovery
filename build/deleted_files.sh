partition=$1
sudo fls -r -d $partition 2 > /usr/tmp/iKnowdeDiscovery/deleted_files.txt
python report_deleted_files.py

