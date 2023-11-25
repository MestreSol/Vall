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
from src.controller.InstituicaoController import InstituicaoController

from src.model.Professor import Professor
from src.model.Aluno_turma import Aluno_turma
from src.model.Aula import Aula
from src.model.Disciplina import Disciplina
from src.model.Frequencia import Frequencia
from src.model.Nota import Nota
from src.model.Turma import Turma
from src.model.Aluno import Aluno


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
api.add_resource(InstituicaoController, '/instituicoes', '/instituicoes/<int:id>')

# %%
# Professor Routes
@app.route('/professor/name/<string:nome>')
def get_professor_by_name(nome):
    professor = Professor.query.filter_by(nome=nome).first()
    if professor:
        return professor.to_dict(), 200
    else:
        return {"error": "Professor not found"}, 404
@app.route('/professor/email/<string:email>' )
def get_professor_by_email(email):
    professor = Professor.query.filter_by(email=email).first()
    if professor:
        return professor.to_dict(), 200
    else:
        return {"error": "Professor not found"}, 404

# %%
# Aluno_turma Routes
@app.route('/aluno_turma/aluno/<int:id_aluno>' )
def get_aluno_turma_by_aluno(id_aluno):
    aluno_turma = Aluno_turma.query.filter_by(id_aluno=id_aluno).first()
    if aluno_turma:
        return aluno_turma.to_dict(), 200
    else:
        return {"error": "Aluno_turma not found"}, 404
@app.route('/aluno_turma/turma/<int:id_turma>'  )
def get_aluno_turma_by_turma(id_turma):
    aluno_turma = Aluno_turma.query.filter_by(id_turma=id_turma).first()
    if aluno_turma:
        return aluno_turma.to_dict(), 200
    else:
        return {"error": "Aluno_turma not found"}, 404

# %%
# Aula Routes
@app.route('/aula/data/<string:data>' )
def get_aula_by_data(data):
    aula = Aula.query.filter_by(data=data).first()
    if aula:
        return aula.to_dict(), 200
    else:
        return {"error": "Aula not found"}, 404
@app.route('/aula/turma/<int:id_turma>' )
def get_aula_by_turma(id_turma):
    aula = Aula.query.filter_by(id_turma=id_turma).first()
    if aula:
        return aula.to_dict(), 200
    else:
        return {"error": "Aula not found"}, 404

# %%
# Disciplina Routes
@app.route('/disciplina/nome/<string:nome>' )
def get_disciplina_by_nome(nome):
    disciplina = Disciplina.query.filter_by(nome=nome).first()
    if disciplina:
        return disciplina.to_dict(), 200
    else:
        return {"error": "Disciplina not found"}, 404

# %%
# Frequencia Routes
@app.route('/frequencia/aula/<int:id_aula>' )
def get_frequencia_by_aula(id_aula):
    frequencia = Frequencia.query.filter_by(id_aula=id_aula).first()
    if frequencia:
        return frequencia.to_dict(), 200
    else:
        return {"error": "Frequencia not found"}, 404
@app.route('/frequencia/aluno/<int:id_aluno>' )
def get_frequencia_by_aluno(id_aluno):
    frequencia = Frequencia.query.filter_by(id_aluno=id_aluno).first()
    if frequencia:
        return frequencia.to_dict(), 200
    else:
        return {"error": "Frequencia not found"}, 404
@app.route('/frequencia/aula/<int:id_aula>/aluno/<int:id_aluno>' )
def get_frequencia_by_aula_aluno(id_aula, id_aluno):
    frequencia = Frequencia.query.filter_by(id_aula=id_aula, id_aluno=id_aluno).first()
    if frequencia:
        return frequencia.to_dict(), 200
    else:
        return {"error": "Frequencia not found"}, 404

# %%
# Nota Routes
@app.route('/nota/aluno/<int:id_aluno>' )
def get_nota_by_aluno(id_aluno):
    nota = Nota.query.filter_by(id_aluno=id_aluno).first()
    if nota:
        return nota.to_dict(), 200
    else:
        return {"error": "Nota not found"}, 404
@app.route('/nota/disciplina/<int:id_disciplina>' )
def get_nota_by_disciplina(id_disciplina):
    nota = Nota.query.filter_by(id_disciplina=id_disciplina).first()
    if nota:
        return nota.to_dict(), 200
    else:
        return {"error": "Nota not found"}, 404
@app.route('/nota/aluno/<int:id_aluno>/disciplina/<int:id_disciplina>' )
def get_nota_by_aluno_disciplina(id_aluno, id_disciplina):
    nota = Nota.query.filter_by(id_aluno=id_aluno, id_disciplina=id_disciplina).first()
    if nota:
        return nota.to_dict(), 200
    else:
        return {"error": "Nota not found"}, 404

# %%
# Turma Routes
@app.route('/turma/nome/<string:nome>' )
def get_turma_by_nome(nome):
    turma = Turma.query.filter_by(nome=nome).first()
    if turma:
        return turma.to_dict(), 200
    else:
        return {"error": "Turma not found"}, 404



@app.route('/Login/<string:username>/<string:password>')
def MakeLogin(username=None, password=None):
        if username and password:
            if username == 'admin' and password == 'admin':
                return {"message": "Login successful"}, 200
            aluno = Aluno.query.filter_by(email=username, senha=password).first()
            professor = Professor.query.filter_by(email=username, senha=password).first()
            
            if aluno:
                return aluno.to_dict(), 200
            elif professor:
                return professor.to_dict(), 200
            else :
                return {"error": "Login failed"}, 404
        else:
            return {"error": "Login failed"}, 404
# %%
# App Start
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
   
  
    app.run()