from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Inicializando o aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindease.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa a modificação do track
app.secret_key = 'eu123'  # Chave secreta para sessões

# Inicializando o banco de dados
db = SQLAlchemy(app)

# Agora você pode importar suas rotas a partir do módulo routes
from app import routes

# Configuração do LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'  # Define qual a rota de login
login_manager.init_app(app)  # Inicializa o LoginManager

# Carregamento do usuário para login
@login_manager.user_loader
def load_user(user_id):
    from app.models import Psicologo  # Importando o modelo dentro da função para evitar circular imports
    return Psicologo.query.get(int(user_id))

# Criar tabelas no banco de dados quando a aplicação for inicializada
with app.app_context():
    db.create_all()

