import sys
from flask import Flask
from flask_restful import Api

from src.controller.ProfessorController import ProfessorController
from src.controller.AlunoTurmaController import AlunoTurmaController
from src.controller.AulaController import AulaController
from src.controller.DisciplinaController import DisciplinaController
from src.controller.FrequenciaController import FrequenciaController
from src.controller.NotaController import NotaController
from src.controller.TurmaController import TurmaController

from src.model.Professor import Professor
from src.model.Aluno_turma import Aluno_turma
from src.model.Aula import Aula
from src.model.Disciplina import Disciplina
from src.model.Frequencia import Frequencia
from src.model.Nota import Nota
from src.model.Turma import Turma

from database import db
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/T_VALL'
db.init_app(app)
api = Api(app)

api.add_resource(ProfessorController, '/professor', '/professor/<int:id>')
api.add_resource(AlunoTurmaController, '/aluno_turma', '/aluno_turma/<int:id>')
api.add_resource(AulaController, '/aula', '/aula/<int:id>')
api.add_resource(DisciplinaController, '/disciplina', '/disciplina/<int:id>')
api.add_resource(FrequenciaController, '/frequencia', '/frequencia/<int:id>')
api.add_resource(NotaController, '/nota', '/nota/<int:id>')
api.add_resource(TurmaController, '/turma', '/turma/<int:id>')

# %%
# Professor Routes
@app.route('/professor/name/<string:nome>')
def get_professor_by_name(nome):
    professor = Professor.query.filter_by(nome=nome).first()
    if professor:
        return professor.to_dict(), 200
    else:
        return {"error": "Professor not found"}, 404
@app.route('/professor/email/<string:email>')
def get_professor_by_email(email):
    professor = Professor.query.filter_by(email=email).first()
    if professor:
        return professor.to_dict(), 200
    else:
        return {"error": "Professor not found"}, 404

# %%
# App Start
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()