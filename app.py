import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Book, User, Room

@app.route("/")
def hello():
    return render_template("welcome.html")
    # return "Welcome to Brian Portland's page!\nI apologize - it's very barebones right now. But here's what you can do:\nGo to https://portland-spike.herokuapp.com/add/room to try adding a room to the database\nGo to https://portland-spike.herokuapp.com/getallrooms to see all currently existing rooms\nGo to https://portland-spike.herokuapp.com/get/room/ followed by an id to see the room with that id\nGo to https://portland-spike.herokuapp.com/remove/room/ followed by an id to remove a room with that id\n"

@app.route("/add")
def add_room():
    lister = request.args.get('lister')
    roommateGender = request.args.get('roommateGender')
    numAvailable = request.args.get('numAvailable')
    pets = request.args.get('pets')
    shared = request.args.get('shared')
    rent = request.args.get('rent')
    ensuite = request.args.get('ensuite')
    try:
        room=Room(
            lister = lister,
            roommateGender = roommateGender,
            numAvailable = numAvailable,
            pets = pets,
            shared = shared,
            rent = rent,
            ensuite = ensuite
        )
        db.session.add(room)
        db.session.commit()
        return "Room added. Room id={}".format(room.id)
    except Exception as e:
	    return(str(e))

@app.route("/getallrooms")
def get_all_rooms():
    try:
        rooms=Room.query.all()
        return  jsonify([e.serialize() for e in rooms])
    except Exception as e:
	    return(str(e))

@app.route("/get/room/<id_>")
def get_room_by_id(id_):
    try:
        room=Room.query.filter_by(id=id_).first()
        return jsonify(room.serialize())
    except Exception as e:
	    return(str(e))


@app.route("/add/form",methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        name=request.form.get('name')
        author=request.form.get('author')
        published=request.form.get('published')
        try:
            book=Book(
                name=name,
                author=author,
                published=published
            )
            db.session.add(book)
            db.session.commit()
            return "Book added. book id={}".format(book.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

@app.route("/add/room",methods=['GET', 'POST'])
def add_room_form():
    if request.method == 'POST':
        lister = request.form.get('lister')
        roommateGender = request.form.get('roommateGender')
        numAvailable = request.form.get('numAvailable')
        pets = request.form.get('pets')
        shared = request.form.get('shared')
        rent = request.form.get('rent')
        ensuite = request.form.get('ensuite')
        try:
            room=Room(
                lister = lister,
                roommateGender = roommateGender,
                numAvailable = numAvailable,
                pets = pets,
                shared = shared,
                rent = rent,
                ensuite = ensuite
            )
            db.session.add(room)
            db.session.commit()
            return "Room added. Room id={}".format(room.id)
        except Exception as e:
            return(str(e))
    return render_template("listroom.html")

if __name__ == '__main__':
    app.run()