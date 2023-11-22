from database import db

class Frequencia(db.Model):
    __tableName__ = "Frequencia"
    
    id_aula = db.Column(db.Integer, db.ForeignKey('Aula.id_aula'), primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('Aluno.id_aluno'), primary_key=True)
    presenca = db.Column(db.Boolean)
    def to_dict(self):
        return {
            'id_aula': self.id_aula,
            'id_aluno': self.id_aluno,
            'presenca': self.presenca
        }