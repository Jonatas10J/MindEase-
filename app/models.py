from app import db
from flask_login import UserMixin

class Empresa(UserMixin, db.Model):
    __tablename__ = 'empresa'

    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(255))
    nome_empresa = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)  # Aqui estamos garantindo que o email seja único
    cnpj = db.Column(db.String(14), unique=True)    # Também garantindo que o CNPJ seja único
    colaboradores = db.Column(db.Integer)
    endereco = db.Column(db.String(255))
    numero = db.Column(db.String(20))
    senha = db.Column(db.String(255))

    def __repr__(self):
        return f'<Empresa {self.nome_empresa}>'


class Psicologo(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)  
    crp = db.Column(db.String(20), unique=True, nullable=False)
    numero = db.Column(db.String(15), nullable=False)
    nome_completo = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(50), nullable=True)
    abordagem = db.Column(db.String(50), nullable=True)
    senha = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Psicologo {self.nome_completo}>"

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    tipo_usuario = db.Column(db.String(50), nullable=False)  # Pode ser 'psicologo' ou 'empresa'

    def __repr__(self):
        return f"<Usuario {self.email}>"

class Func(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Funcionario {self.nome} {self.sobrenome}>'



