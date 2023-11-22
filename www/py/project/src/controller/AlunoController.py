from flask import request
from flask_restful import Resource
from src.model.Aluno import Aluno
from database import db

class AlunoController(Resource):
    def get(self, id=None):
        if id:
            aluno = Aluno.query.get(id)
            if aluno:
                return aluno.to_dict(), 200
            else:
                return {"error": "Aluno not found"}, 404
        else:
            alunos = Aluno.query.all()
            return [aluno.to_dict() for aluno in alunos], 200

    def post(self):
        data = request.get_json()
        aluno = Aluno(**data)
        db.session.add(aluno)
        db.session.commit()
        return aluno.to_dict(), 201

    def put(self, id):
        data = request.get_json()
        aluno = Aluno.query.get(id)
        if aluno:
            aluno.update(**data)
            db.session.commit()
            return aluno.to_dict(), 200
        else:
            return {"error": "Aluno not found"}, 404

    def delete(self, id):
        aluno = Aluno.query.get(id)
        if aluno:
            db.session.delete(aluno)
            db.session.commit()
            return {"message": "Aluno deleted"}, 200
        else:
            return {"error": "Aluno not found"}, 404