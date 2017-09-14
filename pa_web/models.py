# Models
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True)
    deafult = db.Column(db.Boolean, default=False, index=True)
    permission = db.Column(db.Integer,)
    
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name
    # Insert roles in db
    @staticmethod
    def insert_roles():
        roles = {
            'User' : (Permission.FOLLOW |
                      Permission.COMMENT |
                      Permission.WRITE_POST |
                      , True), 
            'SuperUser' : (Permission.FOLLOW |
                           Permission.COMMENT |
                           Permission.WRITE_POST |
                           , False),
            'Administrator' : ( 0xff, False)
        }
        for( r in roles ):
            role = Role.query.filter_by(name=r).first()
            if( role is None ):
                role = Role.(name=r)
            role.permission = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()
        
    
class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_POST = 0x03
    SUPER_USER = 0x04
    ADMINISTRATOR = 0x80
    
    
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    # Constructor
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if( self.role is None):
            if( self.email == current_app,config('PAWEB_ADMIN') ):
                self.role = Role.query.filter_by(permission=0xff).first()
            else:
                slef.role = Role.query.filter_by(default=True).first()
        
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return '<User %r>' % self.username

# Login helper functions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
