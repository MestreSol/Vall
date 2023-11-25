from flask import request
from flask_restful import Resource
from src.model.Aluno import Aluno
from src.model.Professor import Professor
from database import db

class Login(Resource):
    def get(self, username=None, password=None):
        if username and password:
            if username == 'admin' and password == 'admin':
                return {"message": "Login successful"}, 200
            aluno = Aluno.query.filter_by(email=username, senha=password).first()
            professor = Professor.query.filter_by(email=username, senha=password).first()
            
            if aluno:
                return aluno.to_dict(), 200
            elif professor:
                return professor.to_dict(), 200
            else :
                return {"error": "Login failed"}, 404
        else:
            logins = Login.query.all()
            return [login.to_dict() for login in logins], 200