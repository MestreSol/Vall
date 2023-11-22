
from database import db
class Professor(db.Model):
    __tablename__ = 'Professor'

    id_professor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id_professor': self.id_professor,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha
        }