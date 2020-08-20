from flask import Flask, request, Response
from admin.Admin import start_views
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import json
import controllers as ctrl


def create_app(config):
    app = Flask(__name__)

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['FLASK_ADMIN_SWATCH'] = 'paper'
    db = SQLAlchemy(app)

    start_views(app, db)
    Bootstrap(app)

    db.init_app(app)
    config.APP = app

    @app.after_request
    def after_request(response):
        # response.header.add('Access-Control-Allow-Origin', '*')
        # response.header.add('Access-Control-Allow-Headers', 'Content-Type')
        # response.header.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'
        return response

    @app.route('/report', methods=['GET', 'POST'])
    def report():
        state = request.form['state']
        disease = request.form['disease']
        patients = ctrl.reportByState(state, disease)

        return Response(json.dumps(patients, ensure_ascii=False), mimetype='application/json'), 200, {}
