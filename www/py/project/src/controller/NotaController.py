from flask import request
from flask_restful import Resource
from src.model.Nota import Nota
from database import db

class NotaController(Resource):
    def get(self, id=None):
        if id:
            nota = Nota.query.get(id)
            if nota:
                return nota.to_dict(), 200
            else:
                return {"error": "Nota not found"}, 404
        else:
            notas = Nota.query.all()
            return [nota.to_dict() for nota in notas], 200
    def put(self, id):
        data = request.get_json()
        nota = Nota.query.get(id)
        if nota:
            nota.update(**data)
            db.session.commit()
            return nota.to_dict(), 200
        else:
            return {"error": "Nota not found"}, 404
    def delete(self, id):
        nota = Nota.query.get(id)
        if nota:
            db.session.delete(nota)
            db.session.commit()
            return {"message": "Nota deleted"}, 200
        else:
            return {"error": "Nota not found"}, 404
    def post(self):
        data = request.get_json()
        nota = Nota(**data)
        db.session.add(nota)
        db.session.commit()
        return nota.to_dict(), 201