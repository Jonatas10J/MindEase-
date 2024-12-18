# MindEase-
Mindease
Mindease é uma aplicação desenvolvida para facilitar a interação e gestão entre psicólogos e empresas, permitindo um acesso rápido e eficiente às informações e serviços prestados.

Funcionalidades
Login unificado: Permite acesso tanto para psicólogos quanto para empresas.
Gerenciamento de perfis: Perfis distintos para cada tipo de usuário.
Segurança: Senhas protegidas usando hashing.
Banco de dados: Utilização do SQLite para armazenamento local.


Tecnologias Utilizadas
Backend: Flask
Banco de Dados: SQLite
Gerenciamento de Usuários: Flask-Login
Segurança: Werkzeug para hashing de senhas
Versionamento: Git e GitHub

OBS: Para funcionar será necessário instalar as depêndencias do projeto 
pip install flask flask-login flask-sqlalchemy

1. Rotas Principais
Rota de Cadastro de Psicólogos (/cadastro_psicologo)
•	A rota permite o cadastro de psicólogos, verificando se o e-mail já está registrado e se as senhas coincidem.
•	Se o cadastro for bem-sucedido, a senha é criptografada utilizando a função generate_password_hash, e o novo psicólogo é salvo no banco de dados.
Rota de Cadastro de Empresas (/cadastro_empresa)
•	Permite o cadastro de uma empresa, verificando se o e-mail ou CNPJ já estão registrados.
•	As senhas são comparadas e, caso sejam iguais, a senha é criptografada antes de ser armazenada.
Rota de Cadastro de Funcionários (/cadastro_funcionario)
•	O cadastro de funcionários verifica se o funcionário já existe com o mesmo nome e sobrenome.
•	A senha é criptografada antes de ser salva no banco de dados.
Rota de Login (/login)
•	O login autentica tanto psicólogos quanto empresas, verificando se o e-mail e a senha informados são válidos.
•	Para psicólogos, o login é feito utilizando a tabela Psicologo, enquanto para empresas, ele é feito com a tabela Empresa.
Perfil do Funcionário/Empresa
•	As rotas /perfilFuncionario e /perfilEmpresa são responsáveis por renderizar a página de perfil após o login bem-sucedido. Estas rotas utilizam render_template para exibir as páginas correspondentes.
Tabelas de Exibição
•	As rotas /tabela_empresas, /tabela_psicologos, e /tabela_funcionarios são responsáveis por exibir as informações dos registros no banco de dados para empresas, psicólogos e funcionários, respectivamente. Elas buscam os dados da tabela e passam para os templates HTML.

2. Autenticação e Autorização
•	O projeto usa o Flask-Login para gerenciar autenticação de usuários. O LoginManager é configurado para redirecionar os usuários não autenticados para a página de login.
•	As funções login_user, logout_user, e user_loader são utilizadas para autenticar e carregar os usuários com base no user_id.
o	O user_loader carrega o psicólogo utilizando a função load_user, que recebe o user_id e retorna o psicólogo correspondente no banco de dados.

3. Criptografia de Senhas
•	Werkzeug é utilizado para criptografar as senhas antes de armazená-las no banco de dados. O método generate_password_hash é usado para gerar um hash da senha, e o check_password_hash verifica se a senha fornecida corresponde ao hash armazenado.

4. Flash Messages
•	Flash messages são usadas para mostrar mensagens de sucesso ou erro para o usuário, como mensagens de falha no login ou sucesso no cadastro.
•	As mensagens são exibidas utilizando o flash e recuperadas no template com a função get_flashed_messages.

