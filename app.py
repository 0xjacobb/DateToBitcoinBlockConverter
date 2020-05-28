from flask import Flask, render_template, request, jsonify, redirect, url_for
import converter

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
      result = request.form
      datetime_to_block = converter.DateConverter()
      block_height = datetime_to_block.find_corresponding_block(1590659400)

      return render_template("result.html", block_height = block_height)
    
    else:
        return redirect('index')

if __name__ == "__main__":
    app.run()