from database import db

class Instituicao(db.Model):
    id_instituicao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
    
    def to_dict(self):
        return {
            'id_instituicao': self.id_instituicao,
            'nome': self.nome
        }