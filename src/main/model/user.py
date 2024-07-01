from main.app import db, ma

# User Model
class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    branch =  db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self, username, password, name, role, branch):
        self.username = username
        self.name = name
        self.password = password
        self.role = role
        self.branch = branch
        
# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','username','role','branch')

# Init Schema
user_schema = UserSchema()
