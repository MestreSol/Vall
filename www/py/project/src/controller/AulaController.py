from flask import request
from flask_restful import Resource
from src.model.Aula import Aula
from database import db

class AulaController(Resource):
    def get(self, id=None):
        if id:
            aula = Aula.query.get(id)
            if aula:
                return aula.to_dict(), 200
            else:
                return {"error": "Aula not found"}, 404
        else:
            aulas = Aula.query.all()
            return [aula.to_dict() for aula in aulas], 200
        
    def post(self):
        data = request.get_json()
        aula = Aula(**data)
        db.session.add(aula)
        db.session.commit()
        return aula.to_dict(), 201
    
    def put(self, id):
        data = request.get_json()
        aula = Aula.query.get(id)
        if aula:
            aula.update(**data)
            db.session.commit()
            return aula.to_dict(), 200
        else:
            return {"error": "Aula not found"}, 404
        
    def delete(self, id):
        aula = Aula.query.get(id)
        if aula:
            db.session.delete(aula)
            db.session.commit()
            return {"message": "Aula deleted"}, 200
        else:
            return {"error": "Aula not found"}, 404