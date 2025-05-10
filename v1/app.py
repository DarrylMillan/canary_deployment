# Importar la clase flask desde el modulo flask
from flask import Flask, Response

# Crear instancia de la aplicacion flask, esta sera la aplicacion web
app = Flask(__name__)

# Definir ruta raiz '/' y su controlador, esto significa que cuando un usuario accede al dominio principal
# vera esta respuesta
@app.route('/')

def hello():

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Canary Deployment - v1</title>
        <link rel="icon" href="https://cdn-icons-png.flaticon.com/512/481/481873.png" type="image/png">
        <style>
            body {
                background-color: #f0f4f8;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                color: #333;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 0.5em;
            }
            p {
                font-size: 1.2em;
                color: #555;
            }
            img.icon {
                width: 256px;
                height: 256px;
                margin-bottom: 1em;
            }
        </style>
    </head>
    <body>
        <img class="icon" src="https://cdn-icons-png.flaticon.com/512/888/888879.png" alt="Web Icon">
        <h1>¡Hola desde la <strong>Versión 1 (Producción)</strong>!</h1>
        <p>Esta es la demo de producción estable (Canary Deployment usando Docker y NGINX)</p>
    </body>
    </html>
    """

    # Retornar respuesta de aplicacion version 1
    return Response(html, mimetype='text/html')

# Ejecutar aplicacion
if __name__ == '__main__':

    # Ejecutar la aplicacion en todas las interfaces disponibles (0.0.0.0)
    # en el puerto 5000 (puerto por defecto para flask)
    app.run(host = '0.0.0.0', port = 5000)