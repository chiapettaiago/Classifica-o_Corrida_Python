import random

class GeradorNomes():
    def __init__(self):
        self.nomes = [
    "João", "Maria", "Pedro", "Ana", "Lucas", "Laura", "Carlos", "Fernanda",
    "Rafael", "Juliana", "Gabriel", "Isabela", "Matheus", "Camila", "Felipe", "Sofia",
    "Bruno", "Amanda", "Thiago", "Beatriz", "Daniel", "Mariana", "Vinícius", "Patrícia",
    "Gustavo", "Aline", "Rodrigo", "Renata", "Eduardo", "Clara", "Fernando", "Bianca",
    "Leandro", "Letícia", "André", "Vanessa", "Paulo", "Helena", "Ricardo", "Lívia"
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
        ]
        
    def gerar_categoria(self):
        return random.choice(self.categorias)
    
class GeradorIdade():
    def __init__(self):
        self.idade_minima = 18
        self.idade_maxima = 60

    def gerar_idade(self):
        return random.randint(self.idade_minima, self.idade_maxima)


def main():
    gerador = GeradorNomes()
    geradorIdade = GeradorIdade()
    geradorCategoria = GeradorCategoria()
    colocacao_obj = Colocacao()

    nomes = [gerador.gerar_nome() for _ in range(5)]
    ranking_top5 = []
    for idx, nome in enumerate(nomes, start=1):
        colocacao_str = f"{idx}º Lugar"
        idade = geradorIdade.gerar_idade()
        if idx == 1:
            medalha = "Ouro"
        elif idx == 2:
            medalha = "Prata"
        elif idx == 3:
            medalha = "Bronze"
        else:
            medalha = "Sim"
        trofeu = "Sim" if idx <= 5 else "Não"
        ranking_top5.append({
            "colocacao": colocacao_str,
            "idade": idade,
            "corredor": nome,
            "medalha": medalha,
            "categoria": geradorCategoria.gerar_categoria(),
            "trofeu": trofeu,            "premiacao": "R$ 10000" if idx == 1 else "R$ 5000" if idx == 2 else "R$ 3000" if idx == 3 else "R$ 1500" if idx == 4 else "R$ 1000"
        })
    
    print("\n Maratona Cidade Verde 2025 \n")
    print("\n Ranking Principal: \n")
    for corredor_info in ranking_top5:
        print(f"Colocação: {corredor_info['colocacao']}, Nome: {corredor_info['corredor']}, Idade: {corredor_info['idade']}, Medalha: {corredor_info['medalha']}, Troféu: {corredor_info['trofeu']}, Premiação: {corredor_info['premiacao']} \n")
    
    print("\n Ranking da Categoria PCD: \n")
    for i, corredor_pcd in enumerate(ranking_top5[:3], start=1):
        premio_pcd = "R$ 2000" if i == 1 else "R$ 1000" if i == 2 else "R$ 500"
        print(f"Colocação: {corredor_pcd['colocacao']}, Nome: {corredor_pcd['corredor']}, Idade: {corredor_pcd['idade']}, Categoria: {corredor_pcd['categoria']}, Medalha: {corredor_pcd['medalha']}, Troféu: {corredor_pcd['trofeu']}, Premiação: {premio_pcd} \n")

if __name__ == "__main__":
    main()