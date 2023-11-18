from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.controller.ProfessorController import ProfessorController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/T_VALL'
db = SQLAlchemy(app)
api = Api(app)

api.add_resource(ProfessorController, '/professor', '/professor/<int:id>')

if __name__ == '__main__':
    db.create_all()
    app.run()