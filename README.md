# API de Desenvolvimento Web

## Status do Projeto
![Status](https://img.shields.io/badge/status-em%20progresso-yellow)

## Descrição
Esta API foi desenvolvida como parte da matéria de Desenvolvimento Web no Centro Universitário Católica de Santa Catarina. O objetivo é fornecer uma interface para gerenciar dados de uma aplicação web.

## Tecnologias Utilizadas
- Python
- Flask
- SQLite

## Endpoints
### Dados
- `POST /dados` - Adiciona um novo dado. Envie um JSON com os campos 'nome', 'idade' e 'id_cidade'.
- `GET /dados` - Retorna todos os dados da tabela.
- `GET /dados/{id}` - Retorna um dado específico da tabela.
- `DELETE /dados/{id}` - Deleta um dado específico da tabela.
- `PUT /dados/{id}` - Atualiza um dado específico da tabela. Envie um JSON com os campos 'nome', 'idade' e 'id_cidade'.
### Cidades
- `POST /cidades` - Adiciona um novo dado. Envie um JSON com os campos 'cidade_nome' e 'uf'.
- `GET /cidades` - Retorna todos os dados da tabela.
- `GET /cidades/{id}` - Retorna um dado específico da tabela.
- `PUT /cidades/{id}` - Atualiza um dado específico da tabela. Envie um JSON com os campos 'cidade_nome' e 'uf'.
- `DELETE /cidades/{id}` - Deleta um dado específico da tabela.
<br>
<div align="center">
<h3 align="center">Autor</h3>
<table>
  <tr>
    <td align="center"><a href="https://github.com/AoiteFoca"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141975272?v=4" width="115"><br><sub>Nathan Cielusinski</sub></a></td>
  </tr>
</table>