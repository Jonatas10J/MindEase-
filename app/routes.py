from flask import render_template
from app import app
from flask import Flask, render_template, redirect, url_for, request, flash
from app.models import Empresa
from app.models import Psicologo
from werkzeug.security import generate_password_hash
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadEmpresa")
def cadEmpresa():
    return render_template("cadEmpresa.html")

@app.route("/cadPsicologo")
def cad_psicologo():
    return render_template("cadPsicologo.html")

@app.route("/cadFuncionario")
def cad_funcionario():
    return render_template("cadFuncionario.html")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

@app.route("/chat-conversas")
def chat_conversas():
    return render_template("chat-conversas.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/consultas")
def consultas():
    return render_template("consultas.html")

@app.route("/gerenciarplanos")
def gerenciar_planos():
    return render_template("gerenciarplanos.html")

@app.route("/lista-funcionario")
def lista_funcionario():
    return render_template("lista-funcionario.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        psicologo = Psicologo.query.filter_by(email=email).first()
        
        if psicologo:
            if check_password_hash(psicologo.senha, senha):
                login_user(psicologo)
                return redirect(url_for("perfil_funcionario"))
            else:
                flash("Credenciais de psicólogo inválidas", "danger")  # Exibe erro para psicólogo
        else:
            empresa = Empresa.query.filter_by(email=email).first()
            if empresa:
                if check_password_hash(empresa.senha, senha):
                    login_user(empresa)
                    return redirect(url_for("perfil_empresa"))
                else:
                    flash("Credenciais de empresa inválidas", "danger")  # Exibe erro para empresa
            else:
                flash("Nenhum usuário encontrado com esse e-mail", "danger")  # Exibe erro se não encontrar usuário
                
    return render_template("login.html")


@app.route("/perfilEmpresa")
def perfil_empresa():
    return render_template("perfilEmpresa.html")

@app.route("/perfilFuncionario")
def perfil_funcionario():
    return render_template("perfilFuncionario.html")

@app.route("/senhaEmpresa")
def senha_empresa():
    return render_template("senhaEmpresa.html")

@app.route("/telafuncionario")
def tela_funcionario():
    return render_template("telafuncionario.html")

@app.route('/cadastro_psicologo', methods=['GET', 'POST'])
def cadastro_psicologo():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        # Verifica se o email já existe no banco
        if Psicologo.query.filter_by(email=email).first():
            flash("Email já registrado. Tente outro.", "erro")
            return redirect(url_for('cadastro_psicologo'))
        
        senha = data['senha']
        confirmar_senha = data['confirmar_senha']
        
        # Verifique se as senhas coincidem
        if senha != confirmar_senha:
            flash("As senhas não coincidem. Tente novamente.", "erro")
            return redirect(url_for('cadastro_psicologo'))
        
        novo_psicologo = Psicologo(
            email=email,
            crp=data['crp'],
            numero=data['numero'],
            nome_completo=data['nome_completo'],
            especialidade=data['especialidade'],
            abordagem=data['abordagem'],
            senha=generate_password_hash(senha)  # Criptografa a senha
        )

        db.session.add(novo_psicologo)
        db.session.commit()

        flash("Psicólogo cadastrado com sucesso!", "success")
        return redirect(url_for('cadastro_psicologo'))

    return render_template('cadPsicologo.html')



@app.route('/cadastro_empresa', methods=['GET', 'POST'])
def cadastro_empresa():
    if request.method == 'POST':
        data = request.form
        senha = data['senha']
        confirmar_senha = data['confirmar_senha']

        # Verifique se as senhas coincidem
        if senha != confirmar_senha:
            flash("As senhas não coincidem. Tente novamente.", "erro")
            return redirect(url_for('cadastro_empresa'))

        # Verifique se o e-mail ou o CNPJ já existe
        empresa_existente = Empresa.query.filter(
            (Empresa.email == data['email_corporativo']) | 
            (Empresa.cnpj == data['cnpj'])
        ).first()

        if empresa_existente:
            flash("Já existe uma empresa com esse e-mail ou CNPJ. Tente novamente.", "erro")
            return redirect(url_for('cadastro_empresa'))

        nova_empresa = Empresa(
            razao_social=data['razao_social'],
            nome_empresa=data['nome_empresa'],
            email=data['email_corporativo'],
            cnpj=data['cnpj'],
            colaboradores=data['colaboradores'],
            endereco=data['endereco'],
            numero=data['numero'],
            senha=generate_password_hash(senha)  # Criptografa a senha
        )
        db.session.add(nova_empresa)
        db.session.commit()
        flash("Empresa cadastrada com sucesso!", "success")
        return redirect(url_for('cadastro_empresa'))

    return render_template('cadEmpresa.html')

@app.route('/tabela_empresas')
def tabela_empresas():
    empresas = Empresa.query.all()
    return render_template('tabela_empresas.html', empresas=empresas)
  
@app.route('/tabela_psicologos')
def tabela_psicologos():
    psicologos = Psicologo.query.all()
    return render_template('tabela_psicologos.html', psicologos=psicologos)
