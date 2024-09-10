# from crypt import methods,

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return "df"

@app.route('/math', methods=['POST'])
def mat():
    # return "aaaasnsd"
    if(request.method == 'POST'):
        op = request.json['operation']
        op1 = request.json['op1']
        op2 = request.json['op2']
        result = 0
        if(op == 'add'):
            result = op1 + op2
        elif(op == 'sub'):
            result = op1 - op2
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)