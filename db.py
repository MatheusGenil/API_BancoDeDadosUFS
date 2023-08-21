from flask import Flask as fl
from flask import request as rqt
from flask import jsonify as jsf

dbA = fl(__name__)
Usuario = []

class Usuário:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

@dbA.route('/usuario', methods=['POST'])
def setUsuario():
    dado = rqt.json
    cpf = dado['cpf']
    nome = dado['nome']
    data_nascimento = dado['data_nascimento']
    
    Pessoa = Usuário(cpf, nome, data_nascimento)
    Usuario.append(Pessoa)
    return jsf({'mensagem': 'Usuário criado!'})

@dbA.route('/<int:cpf>', methods=['GET'])
def getUsuario(cpf):

    Pessoa = None
    for Pessoa in Usuario:
        if Pessoa.cpf == cpf:
            break

    if Pessoa:
        return jsf({'cpf': Pessoa.cpf, 'nome': Pessoa.nome, 'data_nascimento': Pessoa.data_nascimento})
    return jsf({'mensagem': 'não encontrado'}), 404

if __name__ == '__main__':
    dbA.run(debug=True)
