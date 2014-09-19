#-*- coding:utf-8 -*-
from RCCar import app
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify


@app.route('/')
def index():
    return render_template('main.html')