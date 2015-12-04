from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=False)
    pw_hash = db.Column(db.String(70), index=False, unique=False)
#len(sha256.hexdigest()) = 64
    posts = db.relationship('Posts', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=False)
    description = db.Column(db.String(1024), index=True, unique=False)
    name = db.Column(db.String(120), index=True, unique=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #id of uploader

class Translations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id')) #id of uploader
    translation = db.Column(db.String(1024), index=False, unique=False)
