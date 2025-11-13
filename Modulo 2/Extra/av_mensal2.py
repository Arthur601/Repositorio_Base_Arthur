from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sistem.html")

@app.route('/somar/<int:n1>/<int:n2>')
def som(n1, n2):
    result = n1 + n2
    return f'{n1} + {n2} = {result}'

@app.route('/subtrair/<int:n1>/<int:n2>')
def sub(n1, n2):
    result = n1 - n2
    return f'{n1} - {n2} = {result}'

@app.route('/multiplicar/<int:n1>/<int:n2>')
def mul(n1, n2):
    result = n1 * n2
    return f'{n1} x {n2} = {result}'

@app.route('/dividir/<int:n1>/<int:n2>')
def div(n1, n2):
    if n2 == 0:
        return 'Não existe divisão por Zero!'
    else:
        return f'{n1} / {n2} = {n1 / n2}'

if __name__ == "__main__":
    app.run(debug=True)