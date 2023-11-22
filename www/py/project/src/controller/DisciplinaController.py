from flask import request
from flask_restful import Resource
from src.model.Disciplina import Disciplina
from database import db

class DisciplinaController(Resource):
    def get(self, id=None):
        if id:
            disciplina = Disciplina.query.get(id)
            if disciplina:
                return disciplina.to_dict(), 200
            else:
                return {"error": "Disciplina not found"}, 404
        else:
            disciplinas = Disciplina.query.all()
            return [disciplina.to_dict() for disciplina in disciplinas], 200
    def post(self):
        data = request.get_json()
        disciplina = Disciplina(**data)
        db.session.add(disciplina)
        db.session.commit()
        return disciplina.to_dict(), 201
    def put(self, id):
        data = request.get_json()
        disciplina = Disciplina.query.get(id)
        if disciplina:
            disciplina.update(**data)
            db.session.commit()
            return disciplina.to_dict(), 200
        else:
            return {"error": "Disciplina not found"}, 404
    def delete(self, id):
        disciplina = Disciplina.query.get(id)
        if disciplina:
            db.session.delete(disciplina)
            db.session.commit()
            return {"message": "Disciplina deleted"}, 200
        else:
            return {"error": "Disciplina not found"}, 404
    def post(self):
        data = request.get_json()
        disciplina = Disciplina(**data)
        db.session.add(disciplina)
        db.session.commit()
        return disciplina.to_dict(), 201
        