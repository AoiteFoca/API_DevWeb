from flask import Flask, request, jsonify; 
import sqlite3;

#Cria a instancia do Flask
app = Flask(__name__);

#Configuração do banco de dados sqlite3
DATABASE = 'database.db';

def get_db():
    db = sqlite3.connect(DATABASE); #Driver sqlite3 conecta no banco de dados
    db.row_factory = sqlite3.Row; #As linhas que o sqlite encontrar, ele retorna
    return db; #Retorna db

#Cria a tabela de dados caso ainda não exista
def init_db():
    with app.app_context(): #Pega o contexto da aplicação (flask)
        db = get_db(); #Conecta no banco de dados
        with app.open_resource('schema.sql', mode='r') as f: #abro o schema em modo leitura como 'f'
            db.cursor().executescript(f.read()); #O executor do banco de dados executa o script do schema (f)
        db.commit(); #Comita as alterações no db
        
#Rota root
@app.route('/')
def home(): #Três aspas duplas servem para comentários de multiplas linhas
    return """ 
    <h1>Bem Vindo à API do Nathan</h1>
    <p>Esta API permite que você execute operações na tabela 'dados'.</p>
    <p>Rotas Disponíveis:</p>
    <ul>
        <li>POST /dados - Adiciona um novo dado. Envie um JSON com os campos 'nome' e 'idade'.</li>
        <li>GET /dados - Retorna todos os dados da tabela.</li>
        <li>GET /dados/{id} - Retorna um dado específico da tabela.</li>
        <li>PUT /dados/{id} - Atualiza um dado específico da tabela. Envie um JSON com os campos 'nome' e 'idade'.</li>
        <li>DELETE /dados/{id} - Deleta um dado específico da tabela.</li>
    </ul>
    """
#Rota que inicializa o banco de dados
@app.route('/initdb')
def initialize_db():
    init_db()
    return "Banco de dados inicializado com sucesso!"

#Rota para adicionar um novo dado
@app.route('/dados', methods=['POST'])
def manage_dados():
    if request.method == 'POST':
        nome = request.json.get('nome'); #Buscando parametro nome de um json
        idade = request.json.get('idade'); #Buscando parametro idade de um json

        if not nome or not idade:
            return jsonify({"error": "Por favor, forneça nome e idade"});
        
        try:
            db = get_db(); #Conecta no banco de dados
            cursor = db.cursor(); #Cria um cursor para executar comandos no banco de dados (manipular os dados)
            cursor.execute("INSERT INTO dados (nome, idade) VALUES (?, ?)", (nome, idade)); #Executa um comando SQL executado no db
            db.commit(); #Comita as alterações no banco de dados
            return jsonify({"success": "Dado adicionado com sucesso!"});
        except sqlite3.Error as e: #Caso aconteça algum erro acima, ele cai no except
            return jsonify({"error": str(e)}), 500; #Pega o erro e retorna como string, além de retornar o erro 500 http (erro interno do servidor)
        finally: #Finally é executado sempre, independente se houve erro ou não
            db.close(); #Preciso fechar o meu banco de dados

#Rota para ver os dados
@app.route('/dados', methods=['GET'])
def get_dados():
    if request.method == 'GET':
        try:
            db = get_db(); #Conecta no banco de dados
            cursor = db.cursor(); #Cria um cursor para executar comandos no
            cursor.execute("SELECT * FROM dados"); #Executa um comando SQL executado no db
            dados = cursor.fetchall(); #Pega todos os dados do cursor
            return jsonify([dict(row) for row in dados]); #Retorna os dados em formato JSON
        except sqlite3.Error as e: #Caso aconteça algum erro acima, ele cai no except
            return jsonify({"error": str(e)}), 500; #Pega o erro e retorna como string, além de retornar o erro 500 http (erro interno do servidor)
        finally:
            db.close();

#Rota para buscar um id específico         
@app.route('/dados/<int:dado_id>', methods=['GET'])
def get_dado(dado_id):
    if request.method == 'GET':
        try:
            db = get_db(); #Conecta no banco de dados
            cursor = db.cursor(); #Cria um cursor para executar comandos no
            cursor.execute("SELECT * FROM dados WHERE id = ?", (dado_id,)); #Executa um comando SQL executado no db 
            #A virgula serve para identificar que nao é uma variavel, mas sim um parâmetro
            dado = cursor.fetchone(); #Pega o dado (id) do cursor
            if(dado): #Verifica se dado existe
                return jsonify(dict(dado)); #Retorna os dados em formato JSON
            else:
                return jsonify({'error': 'Dado não encontrado'}); #Retorna os dados em formato JSON
        except sqlite3.Error as e: #Caso aconteça algum erro acima, ele cai no except
            return jsonify({"error": str(e)}), 500; #Pega o erro e retorna como string, além de retornar o erro 500 http (erro interno do servidor)
        finally:
            db.close();

#Rota para excluir dado
@app.route('/dados/<int:dado_id>', methods=['DELETE'])
def del_dado(dado_id):
    if request.method == 'DELETE':
        try:
            db = get_db(); #Conecta no banco de dados
            cursor = db.cursor(); #Cria um cursor para executar comandos no
            cursor.execute("SELECT * FROM dados WHERE id = ?", (dado_id,)); #Executa um comando SQL executado no db 
            #A virgula serve para identificar que nao é uma variavel, mas sim um parâmetro
            dado = cursor.fetchone(); #Pega o dado (id) do cursor
            if(dado): #Verifica se dado existe
                cursor.execute("DELETE FROM dados WHERE id = ?", (dado_id,)); #Executa um comando SQL executado no db
                db.commit(); #Comita as alterações no banco de dados
                return jsonify({"success": "Dado deletado com sucesso!"});
            else:
                return jsonify({'error': 'ID não encontrado'}); #Retorna os dados em formato JSON
        except sqlite3.Error as e: #Caso aconteça algum erro acima, ele cai no except
            return jsonify({"error": str(e)}), 500; #Pega o erro e retorna como string, além de retornar o erro 500 http (erro interno do servidor)
        finally:
            db.close();

#Inicializar o app Flask
if __name__ == '__main__':
    app.run(debug=True); #Roda o app em modo debug