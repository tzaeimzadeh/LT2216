from flask import Flask, render_template, make_response
app = Flask(__name__)

temp = '13'

@app.route('/weather')
def hello():
    vxml = render_template('weather.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/book_flight')
def book_flight():
    vxml = render_template('book_flight.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/delayed_flights')
def delayed_flights():
    vxml = render_template('delayed_flights.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response
