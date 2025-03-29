from flask import Flask, request

app = Flask(__name__)

# Decorador
@app.route('/')
# localhost:5000/?nombre=valor&apellido=valor
def hello_world():
    print(request)
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    return f'<html>Hola {nombre} {apellido}</html>'



# Bruno / laureano dice que esto pisa a lo anterior y se ejecuta esto y va a fallar
@app.route('/usuario/<int:id>/')
def usuario_id(id):
    return f'Hola usuario con id: {id}!'



# Fernando dice que ejecuta acá
@app.route('/usuario/<string:nombre>/')
def usuario(nombre):
    return f'Hola {nombre}!'




# Mateo dice que explota por el aire

@app.route('/ifts')
def ifts():
    return 'chau!'


if __name__ == '__main__':
    app.run()



# Inicio decorador
# Linea 2
# ....
# Linea 10
# hello_world()
# Linea 12
# ...
# Linea 20

