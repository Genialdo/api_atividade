from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Junior', idade=24)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    #for i in pessoa:
    #   print(i.nome)

    #pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    #print(pessoa.idade)

    #for p in pessoa:
    #    print(p)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Junior').first()
    pessoa.nome = 'Emanuel'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Junior').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
