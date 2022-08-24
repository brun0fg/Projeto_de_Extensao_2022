# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    #criar uma variavel com o meu nome
    nome="Bruno da Silva Justinio"
    return render_template("alo.html", n=nome), 200

app.run()