from flask import request
from flask_restful import Resource
from src.model.Insituicao import Instituicao
from database import db

class InstituicaoController(Resource):
    def get(self, id=None):
        if id:
            instituicao = Instituicao.query.get(id)
            if instituicao:
                return instituicao.to_dict(), 200
            else:
                return {"error": "Instituicao not found"}, 404
        else:
            instituicoes = Instituicao.query.all()
            return [instituicao.to_dict() for instituicao in instituicoes], 200
    def post(self):
        data = request.get_json()
        instituicao = Instituicao(**data)
        db.session.add(instituicao)
        db.session.commit()
        return instituicao.to_dict(), 201
    def put(self, id):
        data = request.get_json()
        instituicao = Instituicao.query.get(id)
        if instituicao:
            instituicao.update(**data)
            db.session.commit()
            return instituicao.to_dict(), 200
        else:
            return {"error": "Instituicao not found"}, 404
    def delete(self, id):
        instituicao = Instituicao.query.get(id)
        if instituicao:
            db.session.delete(instituicao)
            db.session.commit()
            return {"message": "Instituicao deleted"}, 200
        else:
            return {"error": "Instituicao not found"}, 404
