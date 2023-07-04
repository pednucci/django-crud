# CRUD Django API

## Base URL
`https://localhost:8000/api/`

## Recursos Disponíveis

### Tarefas [/tarefas]
A API oferece os seguintes métodos para interagir com os recursos de Tarefas:

#### Listar Tarefas [GET]
Retorna uma lista de todas as tarefas.

+ Request (application/json)

    + Headers

            Authorization: Bearer {token}

+ Response 200 (application/json)

        [
            {
                "id": "c058a378-498f-4e6a-b8c5-7ae6c48779f2",
                "titulo": "Tarefa 1",
                "descricao": "Descrição da Tarefa 1",
                "prazo": "2023-07-01",
                "finalizado": false
            },
            {
                "id": "d7e95b18-4d09-42f5-bb82-7ad1f715f7a0",
                "titulo": "Tarefa 2",
                "descricao": "Descrição da Tarefa 2",
                "prazo": "2023-07-05",
                "finalizado": true
            }
        ]

#### Criar Tarefa [POST]
Cria uma nova tarefa.

+ Request (application/json)

    + Headers

            Authorization: Bearer {token}

    + Body

            {
                "titulo": "Nova Tarefa",
                "descricao": "Descrição da Nova Tarefa",
                "prazo": "2023-07-10",
                "finalizado": false
            }

+ Response 201 (application/json)

    + Body

            {
                "id": "f2e31f1d-9673-4be2-892d-3f7c4c6e09bb",
                "titulo": "Nova Tarefa",
                "descricao": "Descrição da Nova Tarefa",
                "prazo": "2023-07-10",
                "finalizado": false
            }

### Tarefa [/tarefas/{id}]
A API oferece os seguintes métodos para interagir com tarefas individuais:

#### Obter Detalhes da Tarefa [GET]
Retorna os detalhes de uma tarefa específica.

+ Parameters
    + id (string, required) - O ID da tarefa

+ Request (application/json)

    + Headers

            Authorization: Bearer {token}

+ Response 200 (application/json)

    + Body

            {
                "id": "c058a378-498f-4e6a-b8c5-7ae6c48779f2",
                "titulo": "Tarefa 1",
                "descricao": "Descrição da Tarefa 1",
                "prazo": "2023-07-01",
                "finalizado": false
            }

#### Atualizar Tarefa [PUT]
Atualiza os detalhes de uma tarefa existente.

+ Parameters
    + id (string, required) - O ID da tarefa

+ Request (application/json)

    + Headers

            Authorization: Bearer {token}

    + Body

            {
                "titulo": "Tarefa Atualizada",
                "descricao": "Descrição da Tarefa Atualizada",
                "prazo": "2023-07-03",
                "finalizado": true
            }

+ Response 200 (application/json)

    + Body

            {
                "id": "c058a378-498f-4e6a-b8c5-7ae6c48779f2",
                "titulo": "Tarefa Atualizada",
                "descricao": "Descrição da Tarefa Atualizada",
                "prazo": "2023-07-03",
                "finalizado": true
            }

#### Deletar Tarefa [POST]
Exclui uma tarefa existente.

+ Parameters
    + id (string, required) - O ID da tarefa

+ Request (application/json)

    + Headers

            Authorization: Bearer {token}

+ Response 204

    No Content

## Autenticação
A API utiliza autenticação baseada em JWT (JSON Web Token). Para acessar os endpoints protegidos, você precisa enviar um token de autenticação no cabeçalho de autorização.

+ Headers

        Authorization: Bearer {token}

Obtenha um token de autenticação fazendo uma requisição para `/api/token/`.

É necessário fornecer um usuário e senha válidos para gerar um token.

Criar um usuário:
/user/create

Body:
{
    "username": "usuario"
    "password": "senha"
}

## Erros
A API retorna os seguintes códigos de erro em caso de falhas:

+ 400 Bad Request - A requisição é inválida ou contém parâmetros inválidos.
+ 401 Unauthorized - Falha na autenticação ou token de acesso inválido.
+ 403 Forbidden - Acesso negado devido a permissões insuficientes.
+ 404 Not Found - O recurso solicitado não foi encontrado.
+ 500 Internal Server Error - Erro interno no servidor.
