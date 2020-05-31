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
      unix_datetime = int(datetime_to_block.get_unix_datetime(input_datetime))
      block_height = datetime_to_block.get_corresponding_block(unix_datetime)
      datetime_back = datetime_to_block.get_backconvertet_datetime(unix_datetime)
      #actual_unix_timestamp = datetime_to_block.get_actual_unix_timestamp()
      actual_unix_timestamp = 0

      return render_template("result.html", block_height = block_height, unix_datetime = unix_datetime, datetime_back = datetime_back, actual_unix_timestamp = actual_unix_timestamp)
    
    else:
        return redirect('index')

if __name__ == "__main__":
    app.run()