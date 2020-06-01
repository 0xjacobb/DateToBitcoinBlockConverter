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
      
      #datetime_back = datetime_to_block.get_backconvertet_datetime(unix_datetime)
      #actual_unix_timestamp = datetime_to_block.get_actual_unix_timestamp()
      actual_unix_timestamp = 0

      return render_template("result.html", user_input_datetime = user_input_datetime,
                                            user_input_datetime_UTC = user_input_datetime_UTC,
                                            unix_datetime = unix_datetime, 
                                            actual_unix_timestamp = actual_unix_timestamp,
                                            block_height = block_height)
    
    else:
        return redirect('index')

if __name__ == "__main__":
    app.run()