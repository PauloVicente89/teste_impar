### Teste tecnico - ÍMPAR

<h3>Instalação</h3>
1. git clone "https://github.com/PauloVicente89/teste_impar"<br/>
2. cd ./teste_impar<br/>
3. Renomeie o arquivo '.env-example' para '.env'<br/>
4. docker-compose -f ./docker-compose-development.yml up --build<br/><br/>

*<b>O arquivo '.env-example' não deveria ter credenciais, mas como estamos num ambiente controlado de testes não vejo porque retirar</b>*

<h3>Documentação</h3>

- Para acessar a documentação da API: <code>http://localhost:8000/docs/</code><br/><br/>

<h3>Credenciais de login</h3>

*<b>Caso haja algum problema inesperado e o ADMIN não exista, crie usando o comando: <code>docker exec -it impar_api python manage.py createsuperuser</code></b>*<br/>

- Administrador:<br/>
email: paulo@admin.com<br/>
senha: Senha@123<br/>

- Usuário comum:<br/>
email: paulo@usuario.com<br/>
senha: Senha@123<br/><br/>


<h3>GraphQL</h3>

- Para acessar ao GraphQL da API: <code>http://localhost:8000/graphql/</code><br/>

<h3>Django ADMIN</h3>

- Para acessar ao Django Admin da API: <code>http://localhost:8000/admin/</code> | <b>Necessário login de Admin</b><br/>

<h3>Rotas restritas para admins:</h3>

- Criação de carros:  <code>/api/cars/create/</code><br/>
- Atualização de carros:  <code>/api/cars/update/<uuid:id>/</code><br/>

<h3>Observações adicionais</h3>

- A Api foi desenvolvida pensando em ser sólido para o usuário, para isso alguns pontos foram construídos:<br/>
1. Na criação/atualização de carros, a rota aceita tanto o UUID de uma 'photo' válida quanto o próprio arquivo da nova foto enviada através de um form-data <br/>
2. Os arquivos Docker estão identificados como arquivos de desenvolvimento, pensando na segregação para quando for para prod<br/>
3. Há um sistema de Autenticação e Autorização já estabelecido, pensando no futuro do projeto<br/>