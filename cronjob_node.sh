#!/bin/bash
#Test
#Author: Marc Steiner
#Date of birth: 08.June.2020
#Further info:
# cron job: update every day at 00:00h --> 0 0 * * * ./cronjob_node.sh
# Authorisation: sudo chmod +x ./cronjob_node.sh
#-------------------------------------------------------------------------------

# log stdout and stderr to two different files
exec >>/var/log/looog.log 2>>/var/log/looog.err.log

# ...and log every command we try to execute to stderr (aka looog.err.log)
set -x

cd /home/DateToBitcoinBlockConverter/DateToBitcoinBlockConverter/
git pull
/home/DateToBitcoinBlockConverter/DateToBitcoinBlockConverter/update_csv.sh >> /home/DateToBitcoinBlockConverter/DateToBitcoinBlockConverter/block-data.csv
git add *
git commit -m "update CSV file - RaspiBlitz"
git push origin master


