# coding=utf-8
import json

from bson import ObjectId
from flask import Flask, url_for, redirect, render_template, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from sqlalchemy import true

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["MONGO_URI"] = "mongodb://localhost:27017/Dictionary_db"
app.config['MONGO_DBNAME'] = 'Dictionary_table'
# app.config['SECRET_KEY'] = 'secret_key'
mongo = PyMongo(app)
db = mongo.db
col = mongo.db["Dictionary_table"]


@app.route('/e-v')
def home():
    if request.method == 'POST':
        en = request.form['en']
        vn = request.form['vn']

        try:

            return redirect('/')
        except:
            return 'Success!!!'

    else:
        mydoc = col.find({})
        return render_template("e-v.html", mydoc=mydoc)
    # mydoc = col.find({"en": "probably"})
    # return render_template("index.html", mydoc=mydoc)


@app.route('/login')
def login():
    return 'hi'


@app.route("/", methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        en = request.form['en']
        vn = request.form['vn']

        try:
            col.insert_many(
                [
                    {
                        "en": en,
                        "vn": vn
                    }
                ])
            return redirect('/')
        except:
            return 'Success!!!'

    else:
        mydoc = col.find({})
        return render_template("admin.html", mydoc=mydoc)
    # return redirect(url_for("login"))


@app.route('/delete/<string:_id>')
def delete(_id):
    try:
        col.delete_one({"_id": ObjectId(_id)})
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


@app.route('/update/<string:_id>', methods=['POST'])
def update(_id):
    en = request.form['en']
    vn = request.form['vn']
    if request.method == 'POST':
        try:
            col.update(
                {"_id": ObjectId(_id)},
                {
                    "en": en,
                    "vn": vn
                },
            )
            return redirect('/')
        except:
            return 'There was a problem updating that task'


@app.route('/updatetabledata/<string:_id>', methods=['GET'])
def update_table_data(_id):
    try:
        x = col.find({"_id": ObjectId(_id)})
        count = 0
        for x1 in x:
            count = count + 1
        if count == 1:
            return jsonify(vn=x1["vn"],
                           en=x1["en"]
                           )
    except:
        return 'There was a problem!'


if __name__ == '__main__':
    app.run(debug=True)
