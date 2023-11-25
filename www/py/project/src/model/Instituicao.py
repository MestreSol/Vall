from database import db

class Instituicao(db.Model):
    __tablename__ = 'Instituicao'

    id_instituicao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id_instituicao': self.id_instituicao,
            'nome': self.nome
        }