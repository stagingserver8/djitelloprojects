from flask import Flask, render_template, request
import jyserver.Flask as jsf
app = Flask(__name__)
from time import sleep
@jsf.use(app)

class App:
    def __init__(self):
        print("hello")

    def connect(self):
        from djitellopy import tello
        self.me = tello.Tello()
        self.me.connect()
        print(self.me.get_battery())
        self.js.document.getElementById('battery').innerHTML = self.me.get_battery()
        self.js.document.getElementById('count').innerHTML = "SYSTEM READY"

    def takeoff(self):
        self.js.document.getElementById('count').innerHTML = "INITIALIZING TAKE OFF. PLS WAIT"
        self.me.takeoff()
        sleep(0.5)
        self.js.document.getElementById('battery').innerHTML = self.me.get_battery()
        self.js.document.getElementById('count').innerHTML = "TAKE OFF SEQUENCE COMPLETE"

    def takeofffromhand(self):
        self.me.initiate_throw_takeoff()
        self.js.document.getElementById('count').innerHTML = "INITIALIZING HAND THROW MODE"
        sleep(0.1)
        self.js.document.getElementById('count').innerHTML = "THROW NOW"


    def land(self):
        self.js.document.getElementById('count').innerHTML = "LANDING SEQUENCE STARTED "
        self.me.land()
        self.js.document.getElementById('count').innerHTML = "LANDING COMPLETED"
        sleep(1)
        self.js.document.getElementById('battery').innerHTML = self.me.get_battery()

    def flipf(self):
        self.me.flip("f")

    def flipb(self):
        self.me.flip("b")

    def enginetest(self):
        self.me.turn_motor_on()
        self.js.document.getElementById('count').innerHTML = "ENGINE BEING TESTED"
        sleep(5)
        self.me.turn_motor_off()
        self.js.document.getElementById('count').innerHTML = "TESTING ENGINE COMPLETED - READY FOR TAKE OFF"

@app.route('/')
def index():
    return App.render(render_template('index.html'))

if __name__ == "__main__":
    app.run(debug=True)

    
