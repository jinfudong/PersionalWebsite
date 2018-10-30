import random

from flask import Blueprint, render_template, session, Response, request, make_response

from APP.ext import models
from APP.models import User, News

home = Blueprint('home', __name__, template_folder="./templates")


@home.route('/')
def home_page():
    resp = make_response(render_template('index.html'))
    return resp


@home.route("/h/")
def show_session():
    st = request.cookies.get("sess_token")
    return st


@home.route('/adduser/')
def add_user():
    user = User()
    user.username = "Tom"
    user.save()
    return '创建成功'


@home.route('/getuser/')
def get_users():
    user = User.query.all()
    print(user)
    for i in user:
        print(i.username)
    return "??"


@home.route("/addnews/")
def add_news():
    n = News()
    n.name = "z%d" % random.randrange(10000)
    n.content = "c%d" % random.randrange(10000)
    n.save()
    return "SUC"


@home.route("/getnews/")
def get_news():
    n = News.query.all()
    data = {
        "news": n,
    }
    return render_template("news_list.html", *data)



