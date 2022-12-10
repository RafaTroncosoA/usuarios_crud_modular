# burgers.py
from usuarios_crud_modularizado import app
from flask import render_template,redirect,request,session,flash
from usuarios_crud_modularizado.models.user import User


@app.route("/")
@app.route("/users")
def index():
    usuarios = User.get_all()
    print(usuarios)
    return render_template("users.html", all_users=usuarios)

@app.route("/new/users")
def add_user():
    return render_template("new_users.html")

@app.route("/add_user", methods=["POST"])
def add_user2():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
        }
    User.save(data)
    return redirect('/users')

@app.route("/delete/<id>")
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/users')

@app.route("/show/<id>")
def show(id):
    data = {'id':id}
    info = User.show(data)[0]
    print(info)
    user_dict = {'id':info['id'],
                 'fn': info['first_name'],
                 'ln': info['last_name'],
                 'email': info['email'],
                 'created': info['created_at'],
                 'updated': info['updated_at']}
    print(user_dict)
    return render_template('show.html',datos = user_dict)

@app.route("/edit/<id>")
def edit_web(id):
    data = {'id':id}
    info = User.show(data)[0]
    return render_template('edit.html',datos = info)

@app.route("/edit_user", methods=['POST'])
def edit():
    print(request.form["id"])
    data = {
        "id":request.form["id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
        }
    User.edit(data)

    return redirect("/show/{}".format(request.form["id"]))
