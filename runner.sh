#!/bin/bash
#cd /Global-statistics
git pull
#pip install --user  # useful if not already installed
mysql --defaults-file=../replica.my.cnf -h meta.analytics.db.svc.wikimedia.cloud meta_p > wiki_list.txt
sed -i '1d' wiki_list.txt # delete first line https://stackoverflow.com/questions/339483/how-can-i-remove-the-first-line-of-a-text-file-using-bash-sed-script
time ./scripter.sh