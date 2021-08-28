from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ExtrasUsuarios(db.Model):
    __tablename__ = 'extrasusuarios'
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), index=True, nullable=True)
    actividad = db.Column(db.String(150))
    fecha = db.Column(db.Date)
    tipo = db.Column(db.String(80))
    descripcion = db.Column(db.String(300))
    URLVideo = db.Column(db.String(200))
    URLFoto = db.Column(db.String(200))

    def __repr__(self):
        return 'Extras usuario %r' % self.actividad

    def serialize(self):
        return {
            "id": self.id,
            "userID": self.userID,
            "actividad": self.actividad,
            "fecha": self.fecha,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "URLVideo": self.URLVideo,
            "URLFoto": self.URLFoto
        }

class TodoUsuario(db.Model):
    __tablename__ = 'todousuario'
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    actividad = db.Column(db.String(150))
    fecha = db.Column(db.Date)
    done = db.Column(db.Boolean)

    def __repr__(self):
        return 'Todo del Usuario %r' % self.actividad

    def serialize(self):
        return {
            "id": self.id,
            "userID": self.userID,
            # "userEmail": self.user.email,
            "actividad": self.actividad,
            "fecha": self.fecha,
            "done": self.done
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(9000), unique=False, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    desafio = db.Column(db.String(80), nullable=True)
    toDo_Usuario = db.relationship('TodoUsuario', lazy=True)
    extras_usuario = db.relationship('ExtrasUsuarios', backref='user', lazy=True)

    def __repr__(self):
        return 'Usuario %r' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "desafio": self.desafio,
            "to-do del usuario": self.getUserTodo(),
            "extras del usuario": self.getUserExtras()
        }
    
    def getUserTodo(self):
        return list(map(lambda todo: todo.serialize(), self.toDo_Usuario))

    def getUserExtras(self):
        return list(map(lambda extras: extras.serialize(), self.extras_usuario))

class Extras(db.Model):
    __tablename__ = 'extras'
    id = db.Column(db.Integer, primary_key=True)
    actividad = db.Column(db.String(80), unique=True, nullable=False)
    tipo = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    urlVideo = db.Column(db.String(250), unique=True, nullable=False)
    urlFoto = db.Column(db.String(250), unique=True, nullable=False) 
    dia = db.Column(db.ForeignKey('dias.id'), nullable=True)
    # dia_a_la_que_pertenece = db.relationship('Dias', backref="extras", lazy=True)

    def __repr__(self):
        return 'Extra %r' % self.actividad

    def serialize(self):
        return {
            "id": self.id,
            "actividad": self.actividad,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "urlVideo": self.urlVideo,
            "urlFoto": self.urlFoto
        }

class TemplateTodo(db.Model):
    __tablename__ = 'templatetodo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    idDia = db.Column(db.Integer, db.ForeignKey('dias.id'), nullable=True)

    def __repr__(self):
        return 'To-do (Template) %r' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "idDia": self.idDia
        }

class Dias(db.Model):
    __tablename__ = 'dias'
    id = db.Column(db.Integer, primary_key=True)
    numeroDia = db.Column(db.Integer, nullable=False)
    idDesafio = db.Column(db.ForeignKey('desafios.id'), nullable=True)
    extras_del_dia = db.relationship('Extras', lazy=True)
    # idExtra = db.Column(db.ForeignKey('extras.id'), nullable=True)
    todo_template_del_dia = db.relationship('TemplateTodo', backref='dias', lazy=True)

    def __repr__(self):
        return 'Dia %r' % self.numeroDia

    def serialize(self):
        return {
            "id": self.id,
            "numeroDia": self.numeroDia,
            "idDesafio": self.desafios.nombreDesafio,
            "receta/rutina": self.getExtras(),
            "to-dos del dia": self.getToDos()
        }
    
    def getToDos(self):
        return list(map(lambda todos : todos.serialize(), self.todo_template_del_dia))

    def getExtras(self):
        return list(map(lambda extras : extras.serialize(), self.extras_del_dia))

class Desafios(db.Model):
    __tablename__ = 'desafios'
    id = db.Column(db.Integer, primary_key=True)
    nombreDesafio = db.Column(db.String(80), unique=True, nullable=False)
    descripcionDesafio = db.Column(db.String(250), unique=True, nullable=False)
    feat1 = db.Column(db.String(120), unique=False, nullable=False)
    feat2 = db.Column(db.String(120), unique=False, nullable=False)
    feat3 = db.Column(db.String(120), unique=False, nullable=False)
    photoURL = db.Column(db.String(250), unique=True, nullable=False)
    dias_del_desafio = db.relationship('Dias', backref='desafios', lazy=True)
    
    def __repr__(self):
        return self.nombreDesafio

    def serialize(self):
        return {
            "id": self.id,
            "nombreDesafio": self.nombreDesafio,
            "descripcion": self.descripcionDesafio,
            "feat1": self.feat1,
            "feat2": self.feat2,
            "feat3": self.feat3,
            "photoURL": self.photoURL,
            "dias del desafio": self.getDias()
        }
    
    def getDias(self):
        return list(map(lambda days : days.serialize(),self.dias_del_desafio))
