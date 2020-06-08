from flask import Flask, render_template, request, jsonify, redirect, url_for
import converter
import sys

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
      input_datetime = request.form
      datetime_to_block = converter.DateConverter()

      user_input_datetime = datetime_to_block.get_datetime(input_datetime)
      user_input_datetime_UTC = datetime_to_block.get_datetime_UTC(input_datetime)

      unix_datetime = int(datetime_to_block.get_unix_datetime(input_datetime))
      block_height = datetime_to_block.get_corresponding_block(unix_datetime)
      latest_update = datetime_to_block.get_latest_block_time_CSV()

      link_mainblock = 'https://www.blockchain.com/btc/block/'+ block_height
      link_next_block = 'https://www.blockchain.com/btc/block/'+ str(int(block_height) + 1)

      return render_template("result.html", latest_update = latest_update,
                                            user_input_datetime = user_input_datetime,
                                            user_input_datetime_UTC = user_input_datetime_UTC,
                                            unix_datetime = unix_datetime, 
                                            block_height = block_height,
                                            link_mainblock = link_mainblock,
                                            link_next_block = link_next_block)
    
    else:
        return redirect('index')

if __name__ == "__main__":
    app.run()