#Endpoints de referencia

#ya no es necesario este endpoint, puesto si hacemos POST para users, deberia ser con hash
# @app.route('/users', methods=['POST'])
# @jwt_required()
# def post_users():
#     body = request.get_json()
#     print(body)
#     user = User(email=body['email'],nombre=body['nombre'],password=body['password'])
#     db.session.add(user)
#     db.session.commit()
#     response_body = {
#         "msg": "Hello, this is your POST /user response "
#     }


#     return jsonify(response_body), 200

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

#@app.route('/user', methods=['GET'])
#def handle_hello():
#
#    response_body = {
#        "msg": "Hello, this is your GET /user response "
#    }
#
#    return jsonify(response_body), 200