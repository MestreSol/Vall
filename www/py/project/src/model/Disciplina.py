from database import db

class Disciplina(db.Model):
    id_disciplina = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
    def to_dict(self):
        return {
            'id_disciplina': self.id_disciplina,
            'nome': self.nome
        }