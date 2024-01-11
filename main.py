from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['GET'])  # Ruta cambiada a /hello para evitar conflictos con la ruta por defecto '/'
def hello_world():
    return "Hello World"  # Asegúrate de que este retorno esté correctamente indentado dentro de la función

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Especificar el puerto es opcional, Heroku asignará uno automáticamente
