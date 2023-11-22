from database import db

class Aula(db.Model):
    id_aula = db.Column(db.Integer, primary_key=True)
    id_turma = db.Column(db.Integer, db.ForeignKey('Turma.id_turma'))
    id_professor = db.Column(db.Integer, db.ForeignKey('Professor.id_professor'))
    data = db.Column(db.Date)
    
    def to_dict(self):
        return {
            'id_aula': self.id_aula,
            'id_turma': self.id_turma,
            'id_professor': self.id_professor,
            'data': self.data
        }