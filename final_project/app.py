from flask import Flask, render_template, make_response, send_from_directory
import random

app = Flask(__name__)

#the audio URI and the title of the movie the song is from
song = [("audio/UnderTheSea.pcm", "little mermaid"), ("audio/IWontSayImInLove.pcm", "hercules"), ("audio/HakunaMatata2.pcm", "lion king"),
        ("audio/JustAroundTheRiverbend.pcm", "pocahontas"), ("audio/ColoursOfTheWind.pcm", "pocahontas"), ("audio/BePrepared.pcm", "lion king")]
title = ["little mermaid", "hercules", "lion king", "pocahontas", "pocahontas", "lion king"]

#the audio URI and the next verse of the song
verse = [("audio/WholeNewWorld.pcm", "no one to tell us no, or where to go"), ("audio/Supercali.pcm", "even though the sound of it is something quite atrocious"),
        ("audio/BareNecessities.pcm", "forget about your worries and your strife"), ("audio/MakeAManOutOfYou.pcm", "with all the strength of a raging fire"),
        ("audio/BeOurGuest.pcm", "put our service to the test"), ("audio/HakunaMatata.pcm", "hakuna matata ain't no passing craze")]
lyrics = ["no one to tell us no, or where to go", "even though the sound of it is something quite atrocious", 
        "forget about your worries and your strife", "with all the strength of a raging fire", 
        "put our service to the test", "hakuna matata ain't no passing craze"]


@app.route('/menu')
def menu():
    vxml = render_template('menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/guess_song')
def guess_song():
    vxml = render_template('guess_song.xml', song=random.choice(song), title=title)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/sing_verse')
def sing_verse():
    vxml = render_template('sing_verse.xml', verse=random.choice(verse), lyrics=lyrics)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/audio/<path:path>')
def send_audio(path):
    return send_from_directory('audio', path)
