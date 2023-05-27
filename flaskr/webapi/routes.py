from app import app
from flask import request, redirect
from domain.Note import Note
from persistence.database import Notes

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'
    
# Great route to start with
@app.route('/<string:copy>', methods=['GET'])
def echo(copy):
    return 'Echoing: ' + copy
    
@app.route('/post', methods=['POST'])
def print_post():
    return request.get_json()

@app.route('/<int:id>', methods=['GET'])
def get_board(id):
    if id in Notes.keys():
        notes = Notes[id]

        debug = ""
        for note in notes:
            debug += str(note) + "\n\n"

        return "Found notes: " + debug
    else:
        return "No note found."
    
@app.route('/<int:id>/add', methods=['POST'])
def add_note(id):
    data = request.get_json()
    print(data)
    note = Note(data["Owner"], data["Title"], data["Body"], data["Pos_x"], data["Pos_y"])
    
    if id in Notes.keys():
        Notes[id].append(note)
    else:
        Notes[id] = [note]
    
    return redirect('/'+ str(id))

