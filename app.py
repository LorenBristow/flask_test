# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:41:52 2019

@author: loren
"""

from flask import Flask, render_template, request
app = Flask("MyApp")
@app.route("/")
def hello():
    return "<h1><strong>HI!</strong></h1>"

@app.route("/chicken")
def chicken():
    return "<h1><strong>Cluck Cluck Cluck</strong></h1>"

@app.route("/swimming")
def swimming():
    return "<h1><strong>Splash</strong></h1>"

@app.route("/<name>")
def hello_someone(name):
        return render_template("index.html", name=name.title())

@app.route("/path/to/<pudding>")
def eat_pudding(pudding):
        return render_template("pudding.html", pudding=pudding.title())
        
@app.route("/confirmation", methods=["POST"])
def confirmation():
	form_data = request.form
	result="All OK"
	email = form_data["email"]
	print (form_data["email"])
	#return "All OK"
	return render_template("confirmation.html", title="Form confirmation", **locals())

app.run(debug=True)

