from flask import Flask, render_template, make_response, send_from_directory
import random

app = Flask(__name__)

song = ["song1", "song2", "song3", "song4", "song5", "song6"]


@app.route('/menu')
def menu():
    vxml = render_template('menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/guess_song')
def guess_song():
    vxml = render_template('guess_song.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/sing_verse')
def sing_verse():
    vxml = render_template('sing_verse.xml', form=random.choice(song))
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response
