#!/bin/bash

#Author: Marc Steiner
#Date of birth: 08.June.2020
#Further info:
# cron job: update every day at 00:00h --> 0 0 * * * ./cronjob_node.sh
# Authorisation: sudo chmod +x ./cronjob_node.sh
#-------------------------------------------------------------------------------

git pull
/home/DateToBitcoinBlockConverter/DateToBitcoinBlockConverter/update_csv.sh >> /home/DateToBitcoinBlockConverter/DateToBitcoinBlockConverter/block-data.csv
git add *
git commit -m "update CSV file - RaspiBlitz"
git push origin master


