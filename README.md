# API de Desenvolvimento Web

## Situação do Projeto
![Status](https://img.shields.io/badge/Status-Finalizado-red)

## Descrição
Esta simples API foi desenvolvida como parte da matéria de Desenvolvimento Web no Centro Universitário Católica de Santa Catarina. O objetivo é fornecer opções de /GET,/POST,/PUT,/DELETE para visualizar e gerenciar dados de pessoas e cidades em formato JSON.

## Tecnologias Utilizadas
- Python
- Flask
- SQLite

## Endpoints
### Dados
- `POST /dados` - Adiciona um novo dado. Envie um JSON com os campos 'nome', 'idade' e 'id_cidade'.
- `GET /dados` - Retorna todos os dados da tabela.
- `GET /dados/{id}` - Retorna um dado específico da tabela.
- `PUT /dados/{id}` - Atualiza um dado específico da tabela. Envie um JSON com os campos 'nome', 'idade' e 'id_cidade'.
- `DELETE /dados/{id}` - Deleta um dado específico da tabela.
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
