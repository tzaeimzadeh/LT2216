from flask import Flask, render_template, make_response, send_from_directory
import random

app = Flask(__name__)

#song = ["song1", "song2", "song3", "song4", "song5", "song6"]
song = [("audio/UnderTheSea.pcm", "little mermaid"), ("audio/IWontSayImInLove.pcm", "hercules"), ("audio/HakunaMatata2.pcm", "lion king"),
        ("audio/JustAroundTheRiverbend.pcm", "pocahontas"), ("audio/ColoursOfTheWind.pcm", "pocahontas"), ("audio/BePrePared.pcm", "lion king")]
answers = ["little mermaid", "hercules", "lion king", "pocahontas", "pocahontas", "lion king"]


@app.route('/menu')
def menu():
    vxml = render_template('menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/guess_song')
def guess_song():
    #vxml = render_template('guess_song.xml#'+random.choice(song))
    vxml = render_template('guess_song.xml', song=random.choice(song), answers=answers)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/sing_verse')
def sing_verse():
    #vxml = render_template('sing_verse.xml#'+random.choice(song))
    vxml = render_template('sing_verse.xml', song=random.choice(song), answers=answers)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/audio/<path:path>')
def send_audio(path):
    return send_from_directory('audio', path)
