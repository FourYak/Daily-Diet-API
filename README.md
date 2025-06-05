# Daily Diet API

API para gerenciamento pessoal de dieta diária, permitindo o registro e acompanhamento de refeições com autenticação segura por token JWT.

# Funcionalidades Principais
✅ Cadastro e autenticação de usuários

📝 Registro de refeições com detalhes completos

🔍 Consulta de histórico alimentar

✏️ Edição e exclusão de registros

🔒 Dados protegidos por autenticação JWT

# Tecnologias Utilizadas
Backend: Python com Flask

Banco de Dados: SQLite (pronto para MySQL)

Autenticação: JWT

Validação: Marshmallow

ORM: SQLAlchemy

# Como Configurar
Clone este repositório

Crie e ative um ambiente virtual Python

Instale as dependências com pip install -r requirements.txt

Crie um arquivo .env com sua chave JWT secreta

Execute a aplicação com python app.py

# Endpoints Disponíveis
##Autenticação

POST /register - Cadastra novo usuário

POST /login - Realiza login e retorna token

##Refeições (requer autenticação)

GET /meals - Lista todas refeições do usuário

POST /meals - Adiciona nova refeição

GET /meals/<id> - Detalhes de uma refeição

PUT /meals/<id> - Atualiza refeição

DELETE /meals/<id> - Remove refeição
