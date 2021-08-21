from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoLog(db.Model):
    __tablename__ = 'todolog'
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    todoID = db.Column(db.Integer, db.ForeignKey('templatetodo.id'), nullable=True)
    date = db.Column(db.Date, nullable=True)
    done = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return '<TodoLog %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "done": self.done,
            "desafio": self.desafios.nombreDesafio
        }

class Recetas(db.Model):
    __tablename__ = 'recetas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    urlVideo = db.Column(db.String(250), unique=True, nullable=False)
    urlFoto = db.Column(db.String(250), unique=True, nullable=False) 
    dias_relation = db.relationship('Dias', backref="recetas", lazy=True) 

    def __repr__(self):
        return '<Recetas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "urlVideo": self.urlVideo,
            "urlFoto": self.urlFoto,
            "descripcion": self.descripcion
        }

class TemplateTodo(db.Model):
    __tablename__ = 'templatetodo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    idDia = db.Column(db.Integer, db.ForeignKey('dias.id'), nullable=True)
    todoLog_relation = db.relationship('TodoLog', lazy=True)

    def __repr__(self):
        return '<TemplateTodo %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Rutina(db.Model):
    __tablename__ = 'rutina'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    urlVideo = db.Column(db.String(250), unique=False, nullable=False)
    urlFoto = db.Column(db.String(250), unique=False, nullable=False) 
    dias_relation = db.relationship('Dias', backref="rutina", lazy=True)

    def __repr__(self):
        return '<Rutina %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "urlVideo": self.urlVideo,
            "urlFoto": self.urlFoto,
            "descripcion": self.descripcion
        }

class Dias(db.Model):
    __tablename__ = 'dias'
    id = db.Column(db.Integer, primary_key=True)
    numeroDia = db.Column(db.Integer, nullable=False)
    idDesafio = db.Column(db.ForeignKey('desafios.id'), nullable=True)
    idReceta = db.Column(db.Integer, db.ForeignKey('recetas.id'), nullable=True)
    idRutina = db.Column(db.Integer, db.ForeignKey('rutina.id'), nullable=True)
    todo_t_rel = db.relationship('TemplateTodo', backref='dias', lazy=True)

    def __repr__(self):
        return '<Dias %r>' % self.numeroDia

    def serialize(self):
        return {
            "id": self.id,
            "numeroDia": self.numeroDia,
            "idDesafio": self.idDesafio
        }

class Desafios(db.Model):
    __tablename__ = 'desafios'
    id = db.Column(db.Integer, primary_key=True)
    nombreDesafio = db.Column(db.String(80), unique=True, nullable=False)
    descripcionDesafio = db.Column(db.String(250), unique=True, nullable=False)
    feat1 = db.Column(db.String(120), unique=True, nullable=False)
    feat2 = db.Column(db.String(120), unique=True, nullable=False)
    feat3 = db.Column(db.String(120), unique=True, nullable=False)
    photoURL = db.Column(db.String(250), unique=True, nullable=False)
    dias_rel = db.relationship('Dias', backref='desafios', lazy=True)
    
    def __repr__(self):
        return '<Desafios %r>' % self.nombreDesafio

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
        return list(map(lambda days : days.serialize(),self.dias_rel))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(9000), unique=False, nullable=False)
    todoLog_relation = db.relationship('TodoLog', backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "to-do log": self.getTodoLog()
            # do not serialize the password, its a security breach
        }
    def getTodoLog(self):
        return list(map(lambda todo : todo.serialize(), self.todoLog_relation))