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
from models import db, User, Desafios, Dias, Rutina, TemplateTodo, Recetas, TodoLog
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

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
