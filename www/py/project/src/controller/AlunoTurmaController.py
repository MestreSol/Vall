from flask import request
from flask_restful import Resource
from src.model.Aluno_turma import Aluno_turma
from database import db

class AlunoTurmaController(Resource):
    def get(self, id=None):
        if id:
            aluno_turma = Aluno_turma.query.get(id)
            if aluno_turma:
                return aluno_turma.to_dict(), 200
            else:
                return {"error": "Aluno_turma not found"}, 404
        else:
            alunos_turmas = Aluno_turma.query.all()
            return [aluno_turma.to_dict() for aluno_turma in alunos_turmas], 200

    def post(self):
        data = request.get_json()
        aluno_turma = Aluno_turma(**data)
        db.session.add(aluno_turma)
        db.session.commit()
        return aluno_turma.to_dict(), 201

    def put(self, id):
        data = request.get_json()
        aluno_turma = Aluno_turma.query.get(id)
        if aluno_turma:
            aluno_turma.update(**data)
            db.session.commit()
            return aluno_turma.to_dict(), 200
        else:
            return {"error": "Aluno_turma not found"}, 404

    def delete(self, id):
        aluno_turma = Aluno_turma.query.get(id)
        if aluno_turma:
            db.session.delete(aluno_turma)
            db.session.commit()
            return {"message": "Aluno_turma deleted"}, 200
        else:
            return {"error": "Aluno_turma not found"}, 404