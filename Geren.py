class Animal:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        
    def __str__(self):
        return f"Nome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}"
    
class Canil:
    def __init__(self):
        self.animais = []
        
    def adicionar_animal(self, animal):
        self.animais.append(animal)
        print("Animal adicionado com sucesso!")
        
    def listar_animais(self):
        for i, animal in enumerate(self.animais):
            print(f"Animal {i+1}:")
            print(animal)
            print("--------------------")
            
    def remover_animal(self, indice):
        try:
            animal = self.animais.pop(indice)
            print(f"Animal removido com sucesso:\n{animal}")
        except IndexError:
            print("Índice inválido.")
            
# Exemplo de uso
canil = Canil()
opcao = None

while opcao != "4":
    print("1 - Adicionar animal")
    print("2 - Listar animais")
    print("3 - Remover animal")
    print("4 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        nome = input("Digite o nome do animal: ")
        raca = input("Digite a raça do animal: ")
        idade = input("Digite a idade do animal: ")
        animal = Animal(nome, raca, idade)
        canil.adicionar_animal(animal)
        
    elif opcao == "2":
        canil.listar_animais()
        
    elif opcao == "3":
        indice = int(input("Digite o índice do animal que deseja remover: ")) - 1
        canil.remover_animal(indice)