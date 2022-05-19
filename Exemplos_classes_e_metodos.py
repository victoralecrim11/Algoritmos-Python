# marca, memoria ram, placa de video
# class
# Sintaxe
""""
class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

computador1 = Computador('Asus','8gb','Nvidia')
computador2 = Computador('Dell','10gb','Nvidia')
computador3 = Computador('Acer','16gb','ATM')

print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador1.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador1.placa_de_video)
"""
"""
class computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
         self.marca = marca
         self.memoria_ram = memoria_ram
         self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando...')

    def desligar(self):
        print('estou desligando...')

    def ExibirinformaçõesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = computador('Asus','16gb','Nvidia')
computador1.ligar()
computador1.desligar()
computador1.ExibirinformaçõesDesteComputador()

# Ligar,desligar,exibir Configurações
"""

""""
# Criando a classe carro

class carro:
    # metodo init ou construtor
     def __init__(self,modelo,cor):
         self.modelo = modelo
         self.cor = cor

     def mostrar(self):
        print("O modelo do carro é",self.modelo)
        print("A cor é",self.cor)

# cada objeto vai possuir diferentes self com atributos
audi = carro("Audi A4","Verde")
ferrari = carro("Ferrari 488","Azul")
carro.mostrar(audi)
carro.mostrar(ferrari)
"""

"""
#Criando a classe pessoa

class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def myFunc(self):
        print("Hello my name is " + self.name)

p1 = person("Jhon",36)
p1.myFunc()
""""""

"""
# Usando as palavras mylistobject e abc em vez de self :
""""
class Person:
  def __init__(mylistobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


Herança Python
A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
A classe pai é a classe da qual está sendo herdada, também chamada de classe base.
A classe filha é a classe que herda de outra classe, também chamada de classe derivada.
"""

#Exemplo:
#Crie uma classe chamada Person, com firstnamee lastnamepropriedades e um printnamemétodo:
"""""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

"""

