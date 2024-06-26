from datatime import datetime
from apps.app import db
from werkzeug.security import generate_password_hash

class User(db.model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datatime.now)
    updated_at = db.Column(
        db.DateTime, default=datatime.now, onupdate=datetime.now
    )

    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)