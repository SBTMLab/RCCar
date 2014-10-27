#-*- coding:utf-8 -*-
from RCCar import app
from flask import Flask, request, url_for, abort, render_template
from values import rtmpstring
from RCCar.Control import Control






@app.route('/')
def index():
    return render_template('main.html',rtmpstring=rtmpstring)



@app.route('/stream')
def stream():
	return "nothing"

@app.route('/control', methods=['POST'])
def control():
	key = request.get_json()
	print "hello"
	print key
	

	if '38' in key :
		#UP
		Control.speedup(10)

	if '40' in key :
		#DOWN
		Control.speeddown(10)


	if '37' in key and '39' in key:
		pass

	elif '37' in key :
		#LEFT
		Control.righter()
		

	elif '39' in key:
		#RIGHT
		Control.lefter()

	else :
		Control.center()

	print Control.Direction



	
	return "Sucess"







""" 주요 키코드
up: 38
down: 40
left: 37
right: 39
"""
