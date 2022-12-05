"""
The Observer 👀

Permite que um objeto notifique outros objetos na ocorrência de determinado evento.
Essa funcionalidade permite que objetos se inscrevam a certos eventos.

Por exemplo, cotação do dollar e temperatura

Envolvidos:
-  Subject: representa a entidade na qual os observadores estão interessados 
- Observer: representa todos os objetos que serao notificados quando o estado do Subject mudar

Notificar quando é inserido um produto na classe estoque

Criar classe fornecedor. notificar quando o forncedor enviar um produto, chegou
O fornecedor recebe outra mensagem (recebemos o produto que voce enviou)

Estoque está pronto. Preciso adicionar mais observadores. Basicamente, o que muda, é o atualizar

adicionar mais informação, tipo: numero de envio, etc. (não obrigatório). 

Mensagem forncedor: recebemos o produto x

"""

from abc import ABC, abstractmethod

class Subject(ABC):
    """ Abstract subject """
    def inscrever(self, observer):
      pass
    
    def sair(self, observer):
       pass
    
    def notificar(self):
        pass
  
    
class Estoque(Subject):
    """ Observadores ficaram de olho no estoque """
    # Vetor de strings que representa produtos
    def __init__(self):
        # Variável produtos da classe estoque
        self.produtos = []
        # Variável p/ Salvar os observadores em um lista
        self.observadores = []
    
    def inscrever(self, observer):
        # Verificar se observador ja não está adicionado
        if observer not in self.observadores:
            self.observadores.append(observer)
    
    def sair(self, observer):
        if observer not in self.observadores:
            self.observadores.remove(observer)
    
    def notificar(self):
         # Simple message
        print (f"Notificando observadores {len(self.observadores)}")
        # for loop para percorrer a lista
        for observer in self.observadores:
            # avisar todos os inscritos que algo aconteceu
            observer.atualizar()
        
    def receber_produto(self, produto):
        self.produtos.append(produto)
        self.notificar()


class Observer(ABC):
    """ Abstract Observer """
    # Método ue recebe a notificação
    def atualizar(self):
        pass
    # Método que recebe a notificação
    def notificar_fornecedor(self):
        pass

class Usuario(Observer):
    # Construtor
    def __init__(self, nome, produto=None, subject=None):
        #Inicializar atributos
        self.nome = nome
        # Produto em falta que o usuário está interessado
        self.produto = produto
        # Salvar o estoqur
        self.subject = subject
        # COndição verificar se usuario se inscreveu
        if self.subject:
            # Chamar o método do estoque
            self.subject.inscrever(self)
    
    def atualizar(self):
        # Verificar se é o produto da Joana está contido no estoque | SE TRUE: produto já está no estoque
        if self.produto in self.subject.produtos:
            print(f"[Usuario] {self.nome} notificada")
            print(f"\tSeu produto {self.produto} está disponível")
            
            # Sair da lista de observador
            self.subject.sair(self)

class Fornecedor(Observer):
    def __init__(self, nome, produto=None, subject=None):
        self.nome = nome
        self.produto = produto
        self.subject = subject
        if self.subject:
            self.subject.inscrever(self)
    
    def atualizar(self):
        if self.produto in self.subject.produtos:
            print(f"[Fornecedor] {self.nome} notificado")
            print(f"\tProduto {self.produto} está disponível")
            self.subject.sair(self)
    
    def enviar_produto(self):
        print(f"[Fornecedor] {self.nome} enviando produto")
        self.subject.receber_produto(self.produto)
        self.notificar_fornecedor()
    
    def notificar_fornecedor(self):
        print(f"[Fornecedor] {self.nome} notificado")
        print(f"\tProduto {self.produto} está disponível")
        self.subject.sair(self)
    
        
if __name__ == '__main__':
    print('Observer')
    
class Estoque(Subject):
    
    estoque = Estoque()
    
    # A joana deve se inscrever no sujeito estoque para poder receber a notificação
    Joana = Usuario("Joana", "teclado z", subject=estoque)
    joao = Usuario("Jhona", "Teclado B", subject=estoque)
    
    Lucas = Fornecedor("Lucas", "Teclado D", subject=estoque)
    
    # receber produto
    estoque.receber_produto("Teclado A")
    estoque.receber_produto("Teclado Z")
    estoque.receber_produto("Teclado B")
    
    estoque.notificar_fornecedor("Teclado D")
    
