# mercafacil_proc_seletivo

Esse repositório é referente ao processo seletivo mercafácil

A aplicação está incompleta!

1. Está faltando terminar validações
2. Construir um front-end para consumir a api
3. Authenticação JWT

Como rodar a aplicação
obs: Faz se necessario ter docker e docker-compose instalado
1. Clone esse repositório
2. execute o seguintes comandos
$docker-compose up --build
espero as aplicações subirem e execute
$docker-compose exec web python manage.py migrate --database=varejo
$docker-compose exec web python manage.py migrate --database=macapa

se houver erro ao migrar macapa, espere alguns minutos o mysql está demorando pra inicializar.

3. Pronto a aplicação já esta rodando, você pode acessa-la em localhost:8000

Como não tem front-end, você pode consumir a API com postman, insomnia ou qualquer outro

contatos-macapa.json : http://localhost:8000/contato/macapa/
contatos-varejo.json : http://localhost:8000/contato/varejo/

Está aplicação foi construida com a seguintes tecnologias:
Python, Django, Postgresql, Mysql e Docker

