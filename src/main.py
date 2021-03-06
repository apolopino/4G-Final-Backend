"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, ExtrasUsuarios, TodoUsuario, User, Extras, TemplateTodo, Dias, Desafios
#from models import Person
from werkzeug.security import generate_password_hash, check_password_hash
#nos permite manejar tokens por authentication (usuarios), genera password y las checkea en hash
#es una libreria para python, para que la password no viaje en texto plano y manejarla codificada
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
#crea tokens, indicar una ruta que requiere de un token
import datetime
#nos permite dar tiempo a los tokens, es propio de python
#import hashlib // estan comentados pq no me funcionaron
#from six import ensure_binary // estan comentados pq no me funcionaron
#from hashlib import md5 // estan comentados pq no me funcionaron
import secrets

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'life.planner.web@gmail.com'
app.config['MAIL_PASSWORD'] = 'czqlqkioaclcruoe'

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" with something else!
jwt = JWTManager(app)
mail = Mail(app)

URLFRONTEND = "https://4g-final-front.vercel.app"

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#endpoint para mostrar los desafios
@app.route('/todousuario', methods=['POST'])
#@jwt_required()
def post_todousuario():
    body = request.get_json()
    todousuario = TodoUsuario(
        dia=body['dia'],
        done=False,
        userID=body['uid'],
        actividad=body['actividad']
        )
    db.session.add(todousuario)
    db.session.commit()
    response_body = {
        "msg": "Record added"
    }

    return jsonify(response_body), 200

@app.route('/todousuario', methods=['GET'])
def get_todousuario():
    listatodo = TodoUsuario.query.all()
    listatodo = list(map(lambda x: x.serialize(), listatodo))
    response_body = {
        "msg": "Hello, this is your GET /todousuario response ",
        "lista de to-dos": listatodo

    }
    return jsonify(response_body), 200

@app.route('/todousuario/<int:id>', methods=['GET'])
def get_user_todos(id):

    user = User.query.filter_by(id=id).first()
    user = user.serialize()

    listatodo = user['to-do del usuario']
    
    
    return jsonify(listatodo), 200


@app.route('/todousuario', methods=['PUT'])
def put_user_todos():
    body = request.get_json()
    idtask = body['taskID']

    task = TodoUsuario.query.filter_by(id=idtask).first()
    task.done = True

    db.session.commit() 
    
    return jsonify({
        'msg': "record updated"
    }), 201

# @app.route('/todousuario', methods=['POST'])
# def post_user_todos():
#     body = request.get_json()
#     idDia = body['dia']

#     userTodo = TodoUsuario()

#     userTodo.actividad = body['actividad']
#     userTodo.done = False
#     userTodo.dia = idDia
#     userTodo.userID = body['uid']

#     db.session.commit() 
    
#     return jsonify({
#         'msg': "record created"
#     }), 200
    

@app.route('/extras', methods=['POST'])
#@jwt_required()
def post_extras():
    body = request.get_json()
    element = Extras(
        actividad=body['actividad'],
        tipo=body['tipo'],
        descripcion=body['descripcion'],
        urlVideo=body['urlVideo'],
        urlFoto=body['urlFoto'],
        dia=body['dia']   
        )
    db.session.add(element)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /extras response "
    }

    return jsonify(response_body), 200

@app.route('/extras/<int:id>', methods=['GET'])
def get_user_extras(id):
    # extras = ExtrasUsuarios.query.filter_by(id = ExtrasUsuarios.userID).all()
    # extras = ExtrasUsuarios.query.join(User).filter_by(id=User.id).all()
    # extras = User.query.join(ExtrasUsuarios).filter_by(id = ExtrasUsuarios.userID)
    extras = User.query.filter_by(id=id).all()
    extras = extras[0].extras_usuario
    extras = list(map(lambda x: x.serialize(), extras))
    response_body = {
        "userExtras": extras
    }
    return jsonify(response_body), 200

@app.route('/userextras', methods = ['GET'])
def get_extras_all():
    extras = ExtrasUsuarios.query.all()
    extras = list(map(lambda x: x.serialize(), extras))
    response_body = {
        "extras": extras
    }
    return jsonify(response_body), 200

@app.route('/extras', methods=['GET'])
def get_recetas():
    response = Extras.query.all()
    response = list(map(lambda x: x.serialize(), response))
    response_body = {
        "msg": "Hello, this is your GET /extras response ",
        "extras": response
    }
    return jsonify(response_body), 200

@app.route('/templatetodo', methods=['POST'])
#@jwt_required()
def post_templatetodo():
    body = request.get_json()
    templatetodo = TemplateTodo(
        name=body['name'],
        idDia=body['idDia']
        )
    db.session.add(templatetodo)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /templatetodo response "
    }

    return jsonify(response_body), 200

@app.route('/templatetodo', methods=['GET'])
def get_templatetodo():
    templatetodo = TemplateTodo.query.all()
    templatetodo = list(map(lambda x: x.serialize(), templatetodo))
    response_body = {
        "msg": "Hello, this is your GET /templatetodo response ",
        "templatetodo": templatetodo
    }
    return jsonify(response_body), 200

# POST Dias no logro hacerlo funcionar (no es requerido)
@app.route('/dias', methods=['POST'])
#@jwt_required()
def post_dias():
    body = request.get_json()
    dias = Dias(
        numeroDia=body['numeroDia'],
        idDesafio=body['idDesafio']
        )
    db.session.add(dias)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /dias response "
    }

    return jsonify(response_body), 200

@app.route('/dias', methods=['GET'])
def get_dias():
    dias = Dias.query.all()
    dias = list(map(lambda x: x.serialize(), dias))
    response_body = {
        "msg": "Hello, this is your GET /dias response ",
        "dias": dias
    }
    return jsonify(response_body), 200

@app.route('/desafios', methods=['POST'])
#@jwt_required()
def post_desafios():
    body = request.get_json()
    desafios = Desafios(
        nombreDesafio=body['nombreDesafio'],
        descripcionDesafio=body['descripcionDesafio'],
        feat1=body['feat1'],
        feat2=body['feat2'],
        feat3=body['feat3'],
        photoURL=body['photoURL']
        )
    db.session.add(desafios)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /desafios response "
    }

    return jsonify(response_body), 200

@app.route('/desafios', methods=['GET'])
def get_desafios():
    desafios = Desafios.query.all()
    desafios = list(map(lambda x: x.serialize(), desafios))
    print(desafios)
    response_body = {
        "msg": "Hello, this is your GET /desafios response ",
        "desafios": desafios
    }
    return jsonify(response_body), 200


#endpoint para mostrar los usuarios
@app.route('/users', methods=['GET'])
#@jwt_required()
def get_user():
    users = User.query.all()
    users = list(map(lambda x: x.serialize(), users))
    response_body = {
        "msg": "Hello, this is your GET /Users response ",
        "usuarios": users
    }
    return jsonify(response_body), 200


# endpoint para mostrar un usuario particular
@app.route('/users/<int:id>', methods=['GET'])
#@jwt_required()
def get_user_id(id):
    user = User.query.filter_by(id=id).first()
    print(user)
    
    response_body = {
        "usuario": user
    }
    return jsonify(user.serialize()), 200



""" @app.route('/users/<int:id>', methods=['PUT'])
def put_userupgrade(id):
    user = User.query.get(id)
    request_json = request.get_json()

    user.nombre = request_json["nombre"]
    user.email = request_json["email"]    

    db.session.commit()

    response_body = {
        "msg": "Hello, this is your PUT /user password response "
    }

    return jsonify(response_body), 200 """

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


@app.route("/solicitudrecuperacion", methods=["POST"])
def send_mail():
    email = request.json.get("email")
    print("email:",email)
    user = User.query.filter_by(email=email).first()
    expiracion = datetime.timedelta(days=1)
    if user is not None:
#        access_token = create_access_token(identity=user.email, expires_delta=expiracion)
#        link = URLFRONTEND + "/recuperacion/" + access_token
#        return link
#        h = hashlib.sha1(b"www.recursospython.com - Recursos Python")
#        cadena = 'user.email'
#        h = hashlib.new("md5", "cadena")
#        h = hashlib.md5(b"cadena")
        h = secrets.token_urlsafe(16)
        link = URLFRONTEND + "/solicitudrecuperacion/" + h
        msg = Message("Hello", sender="life.planner.web@gmail.com", recipients=[email])
        msg.body = "Link de recuperacion de contrase??a: " + link 
        mail.send(msg)
        return jsonify({
            "link":"Forgot password link sent"
        }),200
    else: 
        return jsonify({
            "msg": "User does not exist"
        }), 404

@app.route("/nueva_password", methods=["POST"])
#@jwt_required()
def new_password():
    body = request.get_json()
    password = body['password']
    mail = body['email']
    user = User.query.filter_by(email = mail).first()
    pwr_hash = generate_password_hash(password, method='sha256')
    user.password = pwr_hash

    db.session.commit()

    return jsonify({
        "msg": "Password updated successfully"
    }), 201

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

# Endpoint para que un usuario setee su desafio
@app.route('/setchallenge', methods=['PUT'])
def setChallenge():
    body = request.get_json()
    idUser = body['userID']
    usuario = User.query.filter_by(id=idUser).first()
    usuario.desafio = body['desafio']
    usuario.duracion = body['duracion']
    db.session.commit()
    toDos = body['to-do del usuario']
    for item in toDos:
        element = TodoUsuario(
            actividad=item['name'],
            dia=item['idDia'],
            done=item['done'],
            userID=item['userID']
            )
        db.session.add(element)
        db.session.commit()
    extras = body['extras del usuario']
    
    for item in extras:
        elementExtra = ExtrasUsuarios(
            userID=item['userID'],
            actividad=item['actividad'],
            dia=item['dia'],
            tipo=item['tipo'],
            descripcion=item['descripcion'],
            URLVideo=item['urlVideo'],
            URLFoto=item['urlFoto']       
            )
        db.session.add(elementExtra)
        db.session.commit()
    data = {
        "user": usuario.serialize(),
    } 

    return jsonify(data), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
