from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_name = db.Column(db.String(220), unique=False, nullable=False)
    ended = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.todo_name

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def create(cls, request_json):
        todo = cls()
        todo.update(request_json)

        db.session.add(todo)
        db.session.commit()
        return todo
    
    def todo_delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "todo_name": self.todo_name,
            "ended": self.ended
            # do not serialize the password, its a security breach
        }