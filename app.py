import random

class GeradorNomes():
    def __init__(self):
        self.nomes = [
            "João", "Maria", "Pedro", "Ana", "Lucas", "Laura",
            "Carlos", "Fernanda", "Rafael", "Juliana", "Gabriel",
            "Isabela", "Matheus", "Camila", "Felipe", "Sofia"
        ]

    def gerar_nome(self):
        return random.choice(self.nomes)
    
class Colocacao():
    def __init__(self):
        self.colocacoes = [
            "1º Lugar",
            "2º Lugar",
            "3º Lugar",
            "4º Lugar",
            "5º Lugar"
        ]
        
    def gerar_colocacao(self):
        return random.choice(self.colocacoes)
    
class GeradorCategoria():
    def __init__(self):
        self.categorias = [
            "PCD - Deficiência Física",
            "PCD - Deficiência Visual",
            "PCD - Amputados",
            "Pessoa Normal",
        ]
        
    def gerar_categoria(self):
        return random.choice(self.categorias)
    
class GeradorIdade():
    def __init__(self):
        self.idade_minima = 18
        self.idade_maxima = 60

    def gerar_idade(self):
        return random.randint(self.idade_minima, self.idade_maxima)  

class Corredor():
    def __init___(self):
        self.nome = GeradorNomes().gerar_nome()
        self.idade = GeradorIdade().gerar_idade()
        self.categoria = GeradorCategoria().gerar_categoria()
        self.colocacao = Colocacao().gerar_colocacao()
        
    
def main():
    nome = GeradorNomes().gerar_nome()
    idade = random.randint(18, 60)
    colocacao = Colocacao().gerar_colocacao()
    categoria = GeradorCategoria().gerar_categoria()
    premiacao = 0
    medalha = "Ouro" if colocacao == "1º Lugar" else "Prata" if colocacao == "2º Lugar" else "Bronze" if colocacao == "3º Lugar" else "Sim"
    trofeu = "Sim" if colocacao in ["1º Lugar", "2º Lugar", "3º Lugar", "4º Lugar", "5º Lugar"] else "Não"
    if colocacao == "1º Lugar" and categoria == "Pessoa Normal":
        premiacao = 10000
    elif colocacao == "2º Lugar" and categoria == "Pessoa Normal":
        premiacao = 5000
    elif colocacao == "3º Lugar" and categoria == "Pessoa Normal":
        premiacao = 3000
    elif colocacao == "4º Lugar" and categoria == "Pessoa Normal":
        premiacao = 1500
    elif colocacao == "5º Lugar" and categoria == "Pessoa Normal":
        premiacao = 1000
    elif categoria.startswith("PCD"):
        premiacao = 2000 if colocacao == "1º Lugar" else 1000 if colocacao == "2º Lugar" else 500 if colocacao == "3º Lugar" else 0
    
    print(f"Corredor: {nome}, Idade: {idade},  Colocação: {colocacao}, Categoria: {categoria}, Premiação: R${premiacao}, Medalha: {medalha}, Troféu: {trofeu}")
    
if __name__ == "__main__":
    main()