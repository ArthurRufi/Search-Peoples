#create business logic
# NÃO DEVE TER FRAMEWORKS, BIBLIOTECAS, DEPENDENCIAS
# NÃO DEVE TER REQUISIÇÕES, NEM BANCO DE DADOS, NEM ARQUIVOS
# PURAMENTE REGRAS DE NEGÓCIO
# deve ser testável
# criar classe que instancia o objeto pessoa e seus atributos
# criar metodos que devem calcular taxa de sucesso
# criar metodos que devem conferir se a pessoa existe ou não
class Person:
    def __init__(self, name: str, age: int, city: str, mail: str, number: str):
        self.name = name
        self.age = age
        self.city = city
        self.mail = mail
        self.number = number

    def exists(self) -> bool:
        """Confere se a pessoa existe (nome e e-mail não vazios)."""
        return bool(self.name and self.mail)

    def success_rate(self) -> float:
        ... 
        