from models import Pessoas, db_session

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

if __name__ == '__main__':
    insere_pessoas()
    #altera_pessoa()
    consulta_pessoas()
    #exclui_pessoa()