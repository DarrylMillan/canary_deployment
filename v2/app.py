# Importar la clase flask desde el modulo flask
from flask import Flask

# Crear instancia de la aplicacion flask, esta sera la aplicacion web
app = Flask(__name__)

# Definir ruta raiz '/' y su controlador, esto significa que cuando un usuario accede al dominio principal
# vera esta respuesta
@app.route('/')

def hello():

    # Retornar respuesta de aplicacion version 2
    return "Hola desde la versión 2 (canary)", 500

# Ejecutar aplicacion
if __name__ == '__main__':

    # Ejecutar la aplicacion en todas las interfaces disponibles (0.0.0.0)
    # en el puerto 5000 (puerto por defecto para flask)
    app.run(host = '0.0.0.0', port = 5000)