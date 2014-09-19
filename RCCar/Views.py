#-*- coding:utf-8 -*-
from RCCar import app
from flask import Flask, request, url_for, abort, render_template



@app.route('/')
def index():
    return render_template('main.html')



@app.route('/control')
def control():
	key = request.args.get('key',0, type=int)

	if key == 38 :
		#UP
		print "up"

	elif key == 40 :
		#DOWN
		print "down"

	elif key == 37 :
		#LEFT
		print "left"

	elif key == 39 :
		#RIGHT
		print "right"
	else :
		#ELSE
		print "else"


	return "Sucess"





""" 주요 키코드
up: 38
down: 40
left: 37
right: 39
"""
