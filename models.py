from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published':self.published
        }
    
class User(db.Model):
    __tablename__ = 'users'

    name = db.Column(db.String())
    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())
    gender = db.Column(db.String())
    listed = db.Column(db.ARRAY(db.Integer))
    roommateGender = db.Column(db.String())
    pets = db.Column(db.String())
    shared = db.Column(db.String())
    rentMin = db.Column(db.Float)
    rentMax = db.Column(db.Float)
    ensuite = db.Column(db.String())
    favorites = db.Column(db.ARRAY(db.Integer))

    def __init__(name, username, password, gender, listed, roommateGender, pets, shared, rentMin, rentMax, ensuite, favorites):
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.listed = listed
        self.roommateGender = roommateGender
        self.pets = pets
        self.shared = shared
        self.rentMin = rentMin
        self.rentMax = rentMax
        self.ensuite = ensuite
        self.favorites = favorites

    def __repr__(self):
        return '<username {}>'.format(self.username)
    
    def serialize(self):
        return {
            'name': self.name,
            'username': self.username,
            'password': self.password,
            'gender': self.gender,
            'listed': self.listed,
            'roommateGender': self.roommateGender,
            'pets': self.pets,
            'shared': self.shared,
            'rentMin': self.rentMin,
            'rentMax': self.rentMax,
            'ensuite': self.ensuite,
            'favorites': self.favorites
        }

class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    lister = db.Column(db.String())
    roommateGender = db.Column(db.String())
    numAvailable = db.Column(db.Integer)
    pets = db.Column(db.String())
    shared = db.Column(db.String())
    rent = db.Column(db.Float)
    ensuite = db.Column(db.String())

    def __init__(self, lister, roommateGender, numAvailable, pets, shared, rent, ensuite):
        self.lister = lister
        self.roommateGender = roommateGender
        self.numAvailable = numAvailable
        self.pets = pets
        self.shared = shared
        self.rent = rent
        self.ensuite = ensuite

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'lister': self.lister,
            'roommateGender': self.roommateGender,
            'numAvailable': self.numAvailable,
            'pets': self.pets,
            'shared': self.shared,
            'rent': self.rent,
            'ensuite': self.ensuite
        }