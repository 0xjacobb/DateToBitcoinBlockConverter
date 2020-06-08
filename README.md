# DateToBitcoinBlockConverter
## Short Overview
This code takes a specific date in UTC time format and convert it into a new time format, the Bitcoin block number. Becasue Bitcoin blocks are created every 10 minutes in avarage, the conversion is not very precice, but precice enough for some use cases.

It's a flask app running on Heroku: [https://datetime-converter-pro.herokuapp.com/?](https://datetime-converter-pro.herokuapp.com/) 

## Description
The thread describes another issue with the "correct time conversion": [What format is the time of a Bitcoin transaction stored in?](https://bitcoin.stackexchange.com/questions/7788/what-format-is-the-time-of-a-bitcoin-transaction-stored-in#23681)

"There are several things you could mean by the time of the transaction:"
1. When the transaction is created
2. When the transaction is known about by 90% of the network
3. When the transaction is first included into a block
4. When the block is known to 90% of the network

This code does not care about any specific transactions in a block, but more when the block is created.

## Status
Setting up project

## Project Structure
A local Bitcoin node running on a RaspberryPi updates once a day (00:00h) the CSV file via cron job. The RaspberryPi merges automatically the update into the Githup repo which updates the code on Heroku.

```bash
DateToBitcoinBlockConverter
    ├── templates                      # flask searching HTML files in this folder   
    │   └── index.html                 # input site
    │   └── result.html                # shows the corresponding block height  
    ├── .gitignore                     # not tracked files by GIT  
    ├── app.py                         # Flask Web-App   
    ├── block-data.csv                 # file which contains only time_stamp and block_height of all blocks
    ├── converter.py                   # Main file which input and output for web-app
    ├── cronjob_node.sh                # cron job file on local rapberrypi node, which updates CSV file
    ├── mediantime.sh                  # File to get first block data for the CSV file (running once)
    ├── Procfile                       # process file needed for Heroku deployment
    ├── README.md   
    ├── requirements.txt               # all needed dependencies created via: ' pip freeze > requirements.txt '
    ├── runtime.txt                    # define python version for Heroku
    ├── update_csv.sh                  # fetches the newest blocks from a local Bitcoin node via bitcoin-cli. Print out only newest data
```

## Running code local on your Mac
### Installation of Heroku
1. Install Heroku CLI [Link](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3. Check if Heroku it installed with: ```heroku --version```
4. Create an account on Heroku's website
5. After account creation, run in Terminal (maybe run it with admin rights): ```heroku login```
6. Add and deploy app as described here: [Link](https://realpython.com/flask-by-example-part-1-project-setup/)

### Make Code running locally
1. Clone/ download repository
2. cd into project folder

in Terminal (Mac) or CMD (Win):

3. ```pip install virtualenv```   
4. Create virtual environment: ```virtualenv env```
5. Activate virtual environment:   
For macOS: ```source env/bin/activate```   
For Win: Copy in CMD:```"<PATH TO PROJECT>\env\Scripts\activate.bat"``` 
6. Intall dependencies:   
For macOS: ```pip3 install -r requirements.txt```   
For Win: ```pip install -r requirements.txt```   
7. Run app locally:
For macOS: ```python3 app.py```   
For Win: ```python app.py```

## Example
local time input **2009-01-24 00:26:57 (GMT +1: Zürich)** is the same like **2009-01-23 23:26:57 UTC**. The UTC time converter in UNIX is **1232753217**, which results in nearest block **1470**.

## To Do
- [x] First working code with test data
- [x] datetime conversion is not working correct (take local computer time instead of UTC)
- [x] Implement various time zone support (get picked by user)
- [x] Add one block after and one befor found block visible together with URL to blockexplorer
- [ ] Nice UI and credits
- [ ] Make auto-update CSV
- [ ] Make full code running on Heroku
- [ ] Refactoring and implement easier timezone converting without summertime checkbox



## Additional Information
Good time to unix converter: [https://www.unixtime.de/](https://www.unixtime.de/)   
Best Timestamp Converter Onoine [https://www.epochconverter.com](https://www.epochconverter.com)
