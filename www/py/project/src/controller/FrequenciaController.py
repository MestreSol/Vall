from flask import request
from flask_restful import Resource
from src.model.Frequencia import Frequencia
from database import db

class FrequenciaController(Resource):
    def get(self, id=None):
        if id:
            frequencia = Frequencia.query.get(id)
            if frequencia:
                return frequencia.to_dict(), 200
            else:
                return {"error": "Frequencia not found"}, 404
        else:
            frequencias = Frequencia.query.all()
            return [frequencia.to_dict() for frequencia in frequencias], 200
    def post(self):
        data = request.get_json()
        frequencia = Frequencia(**data)
        db.session.add(frequencia)
        db.session.commit()
        return frequencia.to_dict(), 201
    def put(self, id):
        data = request.get_json()
        frequencia = Frequencia.query.get(id)
        if frequencia:
            frequencia.update(**data)
            db.session.commit()
            return frequencia.to_dict(), 200
        else:
            return {"error": "Frequencia not found"}, 404
    def delete(self, id):
        frequencia = Frequencia.query.get(id)
        if frequencia:
            db.session.delete(frequencia)
            db.session.commit()
            return {"message": "Frequencia deleted"}, 200
        else:
            return {"error": "Frequencia not found"}, 404
