import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Utiliza el puerto asignado por Heroku o, por defecto, el 5000
    app.run(host='0.0.0.0', port=port)
