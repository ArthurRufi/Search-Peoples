# vai conectar os entities com contracts
# vai adaptar os dados para o formato que a aplicação espera

from app.Peoples.domain.contracts.peoples import People


class AdapterPeopleTax:
    def __init__(self, name: str, age: int, city: str, mail: str, number: str):
        self.person = People(name, age, city, mail, number)

    # criar um verificador para ver se a pessoa existe no banco de dados a partir de dados fornecidos
    def check_person_exists(self) -> bool:
        return self.person.exists()

    # criar um verificador para ver o valor de entrada e se ele pode ser irreal, por exemplo, irreal uma pessoa ter um paramMoradia > 4, ou seja, mais de 4 casas +
    # + signfica que a pessoa tem 4 casas que torna a busca de endereço irracional, vai calcular porém gerando defict ao inves de acrescimos cirando assim um +
    # + BALANCIADOR DE VALORES *** INTELIGENTE ***
    def calculate_success_rate(self, paramInstagram: float, paramTwitter: float, paramCertidoes: float, paramMoradia: float) -> float:
        return self.person.success_rate(paramInstagram, paramTwitter, paramCertidoes, paramMoradia)

