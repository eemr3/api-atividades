from models import Pessoas, db_session, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Daniel', idade=13)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Tiago').first()
    # print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tiago').first()
    pessoa.nome = 'Tiago'
    pessoa.idade = 22
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tiago').first()
    pessoa.delete()

def insere_uruarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #consulta_pessoas()
    #exclui_pessoa()
    insere_uruarios('eemr3', '1234')
    insere_uruarios('archimonder', '4567')
    consulta_todos_usuarios()