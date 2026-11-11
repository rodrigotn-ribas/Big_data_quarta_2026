class Aluno():

    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, *args) -> None:
        self.notas.extend(args)
    
    def calcular_media(self) -> float:
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

aluno = Aluno("Rodrigo")

aluno.adicionar_nota(10, 8, 9, 7)


print(aluno.calcular_media())