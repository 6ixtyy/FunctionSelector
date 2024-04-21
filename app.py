from flask import Flask, render_template, request
from eth_utils import function_signature_to_4byte_selector
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    function_selector = None
    if request.method == 'POST':
        function_signature = request.form['function_signature']
        selector = function_signature_to_4byte_selector(function_signature)
        function_selector = selector.hex()

    return render_template('index.html', function_selector=function_selector)

if __name__ == '__main__':
    app.run(debug=True)