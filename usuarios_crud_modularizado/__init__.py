# __init__.py
from flask import Flask, render_template,request,redirect
from usuarios_crud_modularizado.models.user import User
app = Flask(__name__)
app.secret_key = "shhhhhh"
