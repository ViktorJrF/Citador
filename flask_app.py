from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    titulo = request.form['titulo']
    revista = request.form['revista']
    processed_text = f'El nombre del autor es: {nombre}, su apellido es: {apellido}, publicó "{titulo}" en {revista}'
    return processed_text

if __name__ == "__main__":
    app.run(debug=True)