from flask import request
from flask_restful import Resource
from src.model.Professor import Professor
from database import db
import json
class ProfessorController(Resource):
    def get(self, id=None):
        if id != None:
            professor = Professor.query.get(id)
            if professor:
                return professor.to_dict(), 200
            else:
                return {"error": "Professor not found"}, 404
        else:
            professores = Professor.query.all()
            return [professor.to_dict() for professor in professores], 200
    def post(self):
        new_professor = Professor(
            nome=request.json['nome'],
            email=request.json['email'],
            senha=request.json['senha'],
            cpf=request.json['cpf'],
            cep=request.json['cep'],
            instituicao=request.json['instituicao'],
            telefone=request.json['telefone']
        )
        db.session.add(new_professor)
        db.session.commit()
        return {'message': 'New professor created.'}, 201

    def put(self, id):
        professor = Professor.query.get(id)
        if professor:
            professor.nome = request.json.get('nome', professor.nome)
            professor.email = request.json.get('email', professor.email)
            professor.senha = request.json.get('senha', professor.senha)
            professor.cpf = request.json.get('cpf', professor.cpf)
            professor.cep = request.json.get('cep', professor.cep)
            professor.instituicao = request.json.get('instituicao', professor.instituicao)
            professor.telefone = request.json.get('telefone', professor.telefone)
            
            db.session.commit()
            return {'message': 'Professor updated.'}
        return {'error': 'Professor not found'}, 404

    def delete(self, id):
        professor = Professor.query.get(id)
        if professor:
            db.session.delete(professor)
            db.session.commit()
            return {'message': 'Professor deleted.'}
        return {'error': 'Professor not found'}, 404
