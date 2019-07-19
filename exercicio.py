#lista de compras de uma pessoa
#dicionario{} uso para por a chave e o valor {'nome' : 'Ana' , 'idade' : 12}trabalham com chaves keys e valores values 
#listas trabalham com posição indices []
#funçoes ()
#kwargs (**) é dicionario e args é listas (*)
#para achar um item em dicionario  .get
#is not != está comparando se há algo dentro .
# crude inserir dados atualizar dados de um site 
#Paradigma orientação á objetos (conjunto de caracteristicas-modo de pensar)
#Para definir os dados são utilizados os atributos, e para definir o comportamento são utilizados métodos.
# Depois que uma classe é definida podem ser criados diferentes objetos que utilizam a classe
#Lista
def lista_compras(pessoa, *args): #segredo é o * 
    print(f'lista de compras {pessoa}:')
    for item in args:
        print(item)
#Dicionario
lista_compras('Joao', 'frango', 'Arroz' ,'sal')
lista_compras('Maria','sacos de lixo')
lista_compras('Fabio' , 'abacate' , 'cenoura')

def lista_telefonica(**kwargs):
    nome = kwargs.get('nome')
    if nome is not None:
        print(f'Na lista tem 1 contato: {nome}')

lista_telefonica(nome = 'Luiza', telefone_Maria = 345345, ramal_Clara = 345544)

#------------------------ORIENTAÇÃO A OBJETOS----------------------------------------#
#Usamos class class gato(animal): a classe cria o objeto por boas praticas a primeira letra do objr é maiuscula
class Animal:
    def __init__(self,nome,dono): #tudo que tem _init_ antes e depois é uma função interna do Python
        self.nome = nome
        self.dono = dono 
#todas a vezes minha funcao init  define meus atributos
#self estou pegando meu argumento ele vai criar um atributo e dar um valor para ele uma propriedade para esse atributo
#encaminha os atributos para seu devido lugar. por exemplo uso nome e dou o parametro de 'Emilly' o self redireciona 
#ele liga e atribui para nome o valor Emilly, "Alocar as coisas na memoria de forma dinamica,aquilo vai ali ou lá..."
#super() significa que estou chamando...... quando eu coloco um _ na frente do atributo significa que estou
#deixando private (privado) e só posso usa-lo nessa documentação

#classes construtoras
#metodos estaticos um método estático é uma atribuição a classe que não precisa do primeiro argumento para ser instanciado na classe. 
#(Normalmente métodos precisam do primeiro argumento como self, para ser uma instância da classe).

