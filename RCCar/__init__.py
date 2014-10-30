#-*- coding:utf-8 -*-
from flask import Flask
import RPIO


app = Flask(__name__)



app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

RPIO.cleanup()


import RCCar.Views
