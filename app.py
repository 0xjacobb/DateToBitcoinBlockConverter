#Author: Marc Steiner
#Date of birth: 26.May.2020
#Further info:

#-------------------------------------------------------------------------------
from flask import Flask, render_template, request
import datetime
import converter
import sys

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    now = datetime.datetime.now()
    return render_template("index.html",
        date = now.date(),
        time = '%s:%s' % (now.hour, now.minute),
        timezone = '0')

@app.route("/result", methods=["POST"])
def result():
    data = request.form

    try:
        datetime_to_block = converter.DateConverter()

        if datetime_to_block:
            user_input_datetime = datetime_to_block.get_datetime(data)
            user_input_datetime_UTC = datetime_to_block.get_datetime_UTC(data)

            unix_datetime = int(datetime_to_block.get_unix_datetime(data))
            block_height = datetime_to_block.get_corresponding_block(unix_datetime)
            latest_update = datetime_to_block.get_latest_block_time_CSV()

            link_mainblock = 'https://www.blockchain.com/btc/block/'+ block_height
            link_next_block = 'https://www.blockchain.com/btc/block/'+ str(int(block_height) + 1)

            return render_template("result.html",
                latest_update = latest_update,
                user_input_datetime = user_input_datetime,
                user_input_datetime_UTC = user_input_datetime_UTC,
                unix_datetime = unix_datetime,
                block_height = block_height,
                link_mainblock = link_mainblock,
                link_next_block = link_next_block)

    except ValueError:
        return render_template("index.html",
            date = data.get('date'),
            time = data.get('time'),
            timezone = data.get('timezone'),
            type_time = data.get('type_time'),
            error = "Please provide values in correct format")

if __name__ == "__main__":
    app.run()
