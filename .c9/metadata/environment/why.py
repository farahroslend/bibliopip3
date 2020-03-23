{"filter":false,"title":"why.py","tooltip":"/why.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'Biblio'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","@app.route('/')","@app.route('/get_UserReviews')","def get_UserReviews():","    return render_template(\"UserReviews.html\", UserReviews=mongo.db.UserReviews.find())",""],"id":80},{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":23},"end":{"row":19,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584296989275,"hash":"06e790ca04c93b35585ec1c920eb03bf94654735"}