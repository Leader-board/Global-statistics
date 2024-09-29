#!/bin/bash
source ../pyvenv/bin/activate
cd /data/project/statanalyser/Global-statistics
sentence="$(<wiki_list.txt)"
# wiki_name = ()
for i in $sentence;
do mysql --defaults-file="$HOME"/replica.my.cnf -h "$i".analytics.db.svc.wikimedia.cloud "$i"_p -e "SELECT user_name, user_registration, user_editcount from user ORDER BY user_editcount desc;" > "${i}".csv;
done
rm -r ../rawcsv
mkdir -p ../rawcsv
mv *.csv ../rawcsv
rm -r ../processed_csv
mkdir -p ../processed_csv
cd "Global user table generator"
time python "global_generator.py"
time python "pushtowiki.py"
time python "user_data.py"