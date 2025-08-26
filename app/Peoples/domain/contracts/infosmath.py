class DeltaInfo:
    def __init__(self, qtd: int):
        self.qtd = qtd


    def delta_social(self) -> float:
        # retornnar 1 siginica match perfeito
        if self.qtd > 4:
            return float(-1.0)
        elif self.qtd >= 1 and self.qtd <= 4:
            return float(self.qtd / 4)
        else:
            return float(-1)
    
    def delta_moradia(self) -> float:
        # retornnar 1 siginica match perfeito
        if self.qtd > 2:
            return float(-1.0)
        elif self.qtd >= 1 and self.qtd <= 4:
            return float(self.qtd / 4)
        else:
            return float(-1.0)
        
    def delta_certidoes(self) -> float:
        #delta de certidoes retornar 3 siginica match perfeito
        if self.qtd > 3:
            return float(3.0)
        elif self.qtd >= 1 and self.qtd <= 3:
            return float(self.qtd / 3)
        else:
            return float(-1.0)

    