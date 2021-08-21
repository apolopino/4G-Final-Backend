"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Desafios, Dias, Rutina, TemplateTodo, Recetas, TodoUsuario
#from models import Person
from werkzeug.security import generate_password_hash, check_password_hash
#nos permite manejar tokens por authentication (usuarios), genera password y las checkea en hash
#es una libreria para python, para que la password no viaje en texto plano y manejarla codificada
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
#crea tokens, indicar una ruta que requiere de un token
import datetime
#nos permite dar tiempo a los tokens, es propio de python

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" with something else!
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/desafios', methods=['GET'])
def get_desafios():
    desafios = Desafios.query.all()
    desafios = list(map(lambda x: x.serialize(), desafios))
    print(desafios)
    response_body = {
        "msg": "Hello, this is your GET /dias response ",
        "desafios": desafios
    }
    return jsonify(response_body), 200

@app.route('/users', methods=['GET'])
#@jwt_required()
def get_user():
    users = User.query.all()
    users = list(map(lambda x: x.serialize(), users))
    response_body = {
        "msg": "Hello, this is your GET /dias response ",
        "usuarios": users
    }
    return jsonify(response_body), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user_id(id):
    user = User.query.filter_by(id=id).first()
    print(user)
    # user = list(map(lambda x: x.serialize(), user))
    response_body = {
        "usuario": user
    }
    return jsonify(user.serialize()), 200

@app.route('/users/<int:id>', methods=['PUT'])
def put_userupgrade(id):
    user = User.query.get(id)
    request_json = request.get_json()

    user.nombre = request_json["nombre"]
    user.email = request_json["email"]    

    db.session.commit()

    response_body = {
        "msg": "Hello, this is your PUT /user password response "
    }

    return jsonify(response_body), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_delete = User.query.get(id)
    if not user_delete:
        response_body = {
            "msg": "Hello, this is your DELETE /user response ",
            "user": "Este user no existe, no puede ser eliminado"
        }
        return jsonify(response_body), 200        
    db.session.delete(user_delete)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your DELETE /user response ",
        "user": "user eliminado"
    }
    return jsonify(response_body), 200    

@app.route('/users', methods=['POST'])
#@jwt_required()
def post_users():
    body = request.get_json()
    print(body)
    user = User(email=body['email'],nombre=body['nombre'],password=body['password'])
    db.session.add(user)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /user response "
    }

    return jsonify(response_body), 200

#ejemplo de breathcode sobre como conseguir un token para un usuario ya creado, como el /hash de ejemplo de Manu
# @app.route('/token', methods=['POST'])
# def create_token():
#     nombre = request.json.get("nombre", None)
#     password = request.json.get("password", None)
#     # Query your database for username and password
#     user = User.filter.query(nombre=nombre, password=password).first()
#     if user is None:
#         # the user was not found on the database
#         return jsonify({"msg": "Bad username or password"}), 401
    
#     # create a new token with the user id inside
#     access_token = create_access_token(identity=user.id)
#     return jsonify({ "token": access_token, "user_id": user.id })

#ruta de ejemplo de breathcode sobre como proteger una ruta a traves del jwt_required()
# @app.route('/protected', methods=['GET'])
# #@jwt_required()
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user_id = get_jwt_identity()
#     user = User.filter.get(current_user_id)
    
#     return jsonify({"id": user.id, "nombre": user.nombre }), 200

#ruta de ejemplo visto en clases JWT sobre como hashear una registro com campos de usuario ya existente
#NO SE USA, implicaria que el usuario se registro sin que su password quedara protegida
#ejemplo de manejo de expiracion
# @app.route('/hash', methods=['GET', 'POST'])
# def handle_hash():
#     # genera token con un hash con expiracion
#     expiracion = datetime.timedelta(days=1)
#     access_token = create_access_token(identity='blbala@gmail.com', expires_delta=expiracion)
#     #aqui se genera el token
      
#     #crear password
#     password = '123456'
#     password =generate_password_hash(password, method='sha256')
#     #genera un password con hash con la libreria werkzeug.security y el algoritmo sha256

#     responde_token = {
#         "users":"prueba", 
#         "token": access_token,
#         "password": password
#     }

#     return jsonify(responde_token), 200

@app.route('/login', methods=['POST'])
def login():
    
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not email:
        return jsonify({"msg":"Email required"}), 400

    if not password:
        return jsonify({"msg":"Password required"}), 400
    
    user = User.query.filter_by(email=email).first()
    print(user)

    if not user:
        return jsonify({"msg": "The email is not correct",
        "status": 401
        
        }), 401

    # password=generate_password_hash(password, method='sha256')

    if not check_password_hash(user.password, password):
         return jsonify({"msg": "The password is not correct",
        "status": 401
        }), 400

    expiracion = datetime.timedelta(days=1)
    access_token = create_access_token(identity=user.email, expires_delta=expiracion)

    data = {
        "user": user.serialize(),
        "token": access_token,
        "expires": expiracion.total_seconds()*1000,
        "userId": user.id,
        "nombre": user.nombre
    }


    return jsonify(data), 200


@app.route('/register', methods=['POST'])
def register():
    
    request_data = request.get_json()

    email = request_data['email']
    password = request_data['password']
    nombre = request_data['nombre']
        
    if not email:
        return "Email required", 401
    if not nombre:
        return "Nombre required", 401
    if not password:
        return "Password required", 401

    
    email_query = User.query.filter_by(email=email).first()
    if email_query:
        return "This email has been already taken", 401
    
    
    user = User()
    user.email = email
    # user.is_active= True
    user.nombre = nombre
    hashed_password=generate_password_hash(password, method='sha256')

    user.password = hashed_password
    print(user)
    db.session.add(user)
    db.session.commit()

    response = {
        "msg": "Added successfully",
        "nombre": nombre,
        "password": hashed_password
    }
    return jsonify(response), 201
#cuando creo un recurso el jsonify es 201


#@app.route('/user', methods=['GET'])
#def handle_hello():
#
#    response_body = {
#        "msg": "Hello, this is your GET /user response "
#    }
#
#    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
