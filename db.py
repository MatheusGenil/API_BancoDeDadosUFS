from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando um armazenamento em memória para os usuários
users = []

class User:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    cpf = data['cpf']
    nome = data['nome']
    data_nascimento = data['data_nascimento']
    
    user = User(cpf, nome, data_nascimento)
    users.append(user)
    
    return jsonify({'message': 'Usuário criado com sucesso!'})

@app.route('/user/<int:cpf>', methods=['GET'])
def get_user(cpf):
    user = next((user for user in users if user.cpf == cpf), None)
    if user:
        return jsonify({'cpf': user.cpf, 'nome': user.nome, 'data_nascimento': user.data_nascimento})
    return jsonify({'message': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
