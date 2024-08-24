CREATE TABLE IF NOT EXISTS dados(
    id integer primary key autoincrement,
    nome text not null,
    idade integer not null,
    id_cidade integer not null,
    foreign key (id_cidade) references cidades(cidade_id)
);
CREATE TABLE IF NOT EXISTS cidades(
    cidade_id integer primary key autoincrement,
    cidade_nome text not null,
    uf text not null
)