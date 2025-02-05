#!/bin/bash
source ../pyvenv/bin/activate
cd /data/project/statanalyser/Global-statistics
#time python "global_generator.py"
time python "pushtowiki.py"
time python "user_data.py"