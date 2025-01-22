### Teste tecnico - ÍMPAR

<h3>Instalação</h3>
1. git clone "https://github.com/PauloVicente89/teste_impar"<br/>
2. cd ./teste_impar<br/>
3. Renomeie o arquivo '.env-example' para '.env'<br/>
4. docker-compose -f ./docker-compose-development.yml up --build<br/>

*<b>O arquivo '.env-example' não deveria ter credenciais, mas como estamos num ambiente controlado de testes não vejo porque retirar</b>*

<h4>Documentação</h4>
- Para acessar a documentação da API: <code>http://localhost:8000/docs/</code><br/>

<h4>Credenciais de login</h4><br/>
*<b>Caso haja algum problema inesperado e o ADMIN não exista, crie usando o comando: 'docker exec -it impar_api python manage.py createsuperuser'</b>*
- Administrador:<br/>
email: paulo@admin.com<br/>
senha: Senha@123<br/>
<br/>
- Usuário comum:<br/>
email: paulo@usuario.com<br/>
senha: Senha@123<br/>


<h4>GraphQL</h4>
- Para acessar ao GraphQL da API: 'http://localhost:8000/graphql/'<br/>

<h4>Django ADMIN</h4>
- Para acessar ao Django Admin da API: 'http://localhost:8000/admin/' | <b>Necessário login de Admin</b><br/>

<h4>Rotas restritas para admins:</h4>
- Criação de carros:  '/api/cars/create/'<br/>

<h4>Observações adicionais</h4>
- A Api foi desenvolvida pensando em ser sólido para o usuário, para isso alguns pontos foram construídos:<br/>
1. Na criação/atualização de carros, a rota aceita tanto o UUID de uma 'photo' válida quanto o próprio arquivo da nova foto enviada através de um form-data <br/>
2. Os arquivos Docker estão identificados como arquivos de desenvolvimento, pensando na segregação para quando for para prod<br/>
3. Há um sistema de Autenticação e Autorização já estabelecido, pensando no futuro do projeto<br/>