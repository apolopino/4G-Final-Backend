from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    todo = db.Column(db.String(120), unique=True, nullable=False)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<ToDo %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "todo": self.todo
        }

class Recetas(db.Model):
    __tablename__ = 'recetas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    videoUrl = db.Column(db.String(250), unique=True, nullable=False)
    imagen = db.Column(db.String(250), unique=True, nullable=False) 
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    dias_relation = db.relationship('Dias', backref="recetas", lazy=True) 
    

    def __repr__(self):
        return '<Recetas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "videoUrl": self.videoUrl,
            "imagen": self.imagen,
            "descripcion": self.descripcion
        }

class TemplateTodo(db.Model):
    __tablename__ = 'templatetodo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    todo1 = db.Column(db.String(80), unique=True, nullable=False)
    todo2 = db.Column(db.String(80), unique=True, nullable=False)
    todo3 = db.Column(db.String(80), unique=True, nullable=False)
    dias_relation = db.relationship('Dias', backref="templatetodo", lazy=True) 

    def __repr__(self):
        return '<TemplateTodo %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "todo1": self.todo1,
            "todo2": self.todo2,
            "todo3": self.todo3
        }

class Rutina(db.Model):
    __tablename__ = 'rutina'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    videoUrl = db.Column(db.String(250), unique=True, nullable=False)
    imagen = db.Column(db.String(250), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    dias_relation = db.relationship('Dias', backref="rutina", lazy=True) 

    def __repr__(self):
        return '<Rutina %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "videoUrl": self.videoUrl,
            "imagen": self.imagen,
            "descripcion": self.descripcion
        }

class Dias(db.Model):
    __tablename__ = 'dias'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desafios_relation = db.relationship('Desafios', backref="dias", lazy=True)
#    idDesafios = db.Column(db.Integer, db.ForeignKey('desafios.id'), nullable=False)
    idRecetas = db.Column(db.Integer, db.ForeignKey('recetas.id'), nullable=False)
    idTemplateTodo = db.Column(db.Integer, db.ForeignKey('templatetodo.id'), nullable=False)
    idRutina = db.Column(db.Integer, db.ForeignKey('rutina.id'), nullable=False)

    def __repr__(self):
        return '<Dias %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Desafios(db.Model):
    __tablename__ = 'desafios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    imagen = db.Column(db.String(250), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), unique=True, nullable=False)
    dificultad = db.Column(db.String(80), unique=True, nullable=False)
    feat1 = db.Column(db.String(120), unique=True, nullable=False)
    feat2 = db.Column(db.String(120), unique=True, nullable=False)
    feat3 = db.Column(db.String(120), unique=True, nullable=False)
#    dias_relation = db.relationship('Dias', backref="desafios", lazy=True)
    idDias = db.Column(db.Integer, db.ForeignKey('dias.id'), nullable=False)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#    user_relation = relationship("User", back_populates="desafios")
    

    def __repr__(self):
        return '<Desafios %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "imagen": self.imagen,
            "descripcion": self.descripcion,
            "dificultad": self.dificultad,
            "feat1": self.feat1,
            "feat2": self.feat2,
            "feat3": self.feat3
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    desafios_relation = db.relationship('Desafios', backref="user", lazy=True)
    todo_relation = db.relationship('ToDo', backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }