#-*- coding:utf-8 -*-
from RCCar import app
from flask import Flask, request, url_for, abort, render_template



@app.route('/')
def index():
    return render_template('main.html')



@app.route('/control', methods=['POST'])
def control():
	key = request.get_json()
	print key

	if '38' in key :
		#UP
		print "up"

	if '40' in key :
		#DOWN
		print "down"

	if '37' in key :
		#LEFT
		print "left"

	if '39' in key:
		#RIGHT
		print "right"


	return "Sucess"





""" 주요 키코드
up: 38
down: 40
left: 37
right: 39
"""
