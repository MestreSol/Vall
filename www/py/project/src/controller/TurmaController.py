from flask import request
from flask_restful import Resource
from src.model.Turma import Turma
from database import db

class TurmaController(Resource):
    def get(self, id=None):
        if id:
            turma = Turma.query.get(id)
            if turma:
                return turma.to_dict(), 200
            else:
                return {"error": "Turma not found"}, 404
        else:
            turmas = Turma.query.all()
            return [turma.to_dict() for turma in turmas], 200
    def post(self):
        data = request.get_json()
        turma = Turma(**data)
        db.session.add(turma)
        db.session.commit()
        return turma.to_dict(), 201
    def put(self, id):
        data = request.get_json()
        turma = Turma.query.get(id)
        if turma:
            turma.update(**data)
            db.session.commit()
            return turma.to_dict(), 200
        else:
            return {"error": "Turma not found"}, 404
    def delete(self, id):
        turma = Turma.query.get(id)
        if turma:
            db.session.delete(turma)
            db.session.commit()
            return {"message": "Turma deleted"}, 200
        else:
            return {"error": "Turma not found"}, 404