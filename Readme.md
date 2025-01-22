### Teste tecnico - ÍMPAR

<h3>Instalação</h3>
1. git clone "https://github.com/PauloVicente89/teste_impar"
2. cd ./teste_impar
3. Renomeie o arquivo '.env-example' para '.env'
4. docker-compose -f ./docker-compose-development.yml up --build

* O arquivo '.env-example' não deveria ter credenciais, mas como estamos num ambiente controlado de testes, não vejo porque retirar *

<h4>Documentação</h4>
- Para acessar a documentação da API: 'http://localhost:8000/docs/'

<h4>Credenciais de login</h4>
* Caso haja algum problema inesperado e o ADMIN não exista, crie usando o comando: 'docker exec -it impar_api python manage.py createsuperuser' *
- Administrador:
email: paulo@admin.com
senha: Senha@123

- Usuário comum:
email: paulo@usuario.com
senha: Senha@123


<h4>GraphQL</h4>
- Para acessar ao GraphQL da API: 'http://localhost:8000/graphql/'

<h4>Django ADMIN</h4>
- Para acessar ao Django Admin da API: 'http://localhost:8000/admin/' | *Necessário login de Admin*

<h4>Rotas restritas para admins:</h4>
- Criação de carros:  '/api/cars/create/'

<h4>Observações adicionais</h4>
- A Api foi desenvolvida pensando em ser sólido para o usuário, para isso alguns pontos foram construídos:
1. Na criação/atualização de carros, a rota aceita tanto o UUID de uma 'photo' válida quanto o próprio arquivo da nova foto enviada através de um form-data
2. Há um sistema de Autenticação e Autorização já estabelecido, pensando no futuro do projeto