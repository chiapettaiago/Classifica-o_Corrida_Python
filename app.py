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
        """Retorna um nome aleatório da lista de nomes disponíveis"""
        return random.choice(self.nomes)
    
class Colocacao():
    """
    Classe para gerenciar as colocações possíveis dos participantes.
    """
    def __init__(self):
        # Lista de colocações para os 5 primeiros lugares
        self.colocacoes = [
            "1º Lugar",
            "2º Lugar",
            "3º Lugar",
            "4º Lugar",
            "5º Lugar"
        ]
        
    def gerar_colocacao(self):
        """Retorna uma colocação aleatória da lista de colocações"""
        return random.choice(self.colocacoes)
    
class GeradorCategoria():
    """
    Classe para gerenciar as categorias PCD disponíveis para os participantes.
    """
    def __init__(self):
        # Lista de categorias PCD disponíveis
        self.categorias = [
            "PCD - Deficiência Física",
            "PCD - Deficiência Visual",
            "PCD - Amputados",
        ]
        
    def gerar_categoria(self):
        """Retorna uma categoria PCD aleatória da lista de categorias"""
        return random.choice(self.categorias)
    
class GeradorIdade():
    """
    Classe para gerar idades aleatórias para os participantes dentro
    de um intervalo específico.
    """
    def __init__(self):
        # Definição da faixa etária permitida para participantes
        self.idade_minima = 18
        self.idade_maxima = 60

    def gerar_idade(self):
        """Retorna uma idade aleatória entre a idade mínima e máxima definidas"""
        return random.randint(self.idade_minima, self.idade_maxima)


def main():
    """
    Função principal que controla a execução do programa.
    Gera os corredores, atribui idades, categorias e prêmios,
    e exibe os resultados nos diferentes rankings.
    """
    # Inicialização dos geradores
    gerador = GeradorNomes()
    geradorIdade = GeradorIdade()
    geradorCategoria = GeradorCategoria()
    colocacao_obj = Colocacao()

    # Geração de 5 nomes aleatórios para os corredores
    nomes = [gerador.gerar_nome() for _ in range(5)]
    ranking_top5 = []
    
    # Criação do ranking com as informações dos 5 primeiros colocados
    for idx, nome in enumerate(nomes, start=1):
        colocacao_str = f"{idx}º Lugar"
        idade = geradorIdade.gerar_idade()
        
        # Determinação da medalha com base na colocação
        if idx == 1:
            medalha = "Ouro"
        elif idx == 2:
            medalha = "Prata"
        elif idx == 3:
            medalha = "Bronze"
        else:
            medalha = "Sim"
            
        # Todos os 5 primeiros recebem troféu
        trofeu = "Sim" if idx <= 5 else "Não"
        
        # Adição do corredor ao ranking com todas suas informações
        ranking_top5.append({
            "colocacao": colocacao_str,
            "idade": idade,
            "corredor": nome,
            "medalha": medalha,
            "categoria": geradorCategoria.gerar_categoria(),
            "trofeu": trofeu,
            # Premiação financeira dependendo da colocação
            "premiacao": "R$ 10000" if idx == 1 else "R$ 5000" if idx == 2 else "R$ 3000" if idx == 3 else "R$ 1500" if idx == 4 else "R$ 1000"
        })
    
    # Exibição dos resultados - Título do evento
    print("\n Maratona Cidade Verde 2025 \n")
    
    # Exibição do ranking principal (top 5 geral)
    print("\n Ranking Principal: \n")
    for corredor_info in ranking_top5:
        print(f"Colocação: {corredor_info['colocacao']}, Nome: {corredor_info['corredor']}, Idade: {corredor_info['idade']}, Medalha: {corredor_info['medalha']}, Troféu: {corredor_info['trofeu']}, Premiação: {corredor_info['premiacao']} \n")
    
    # Exibição do ranking da categoria PCD (apenas os 3 primeiros)
    print("\n Ranking da Categoria PCD: \n")
    for i, corredor_pcd in enumerate(ranking_top5[:3], start=1):
        # Premiações específicas para categoria PCD
        premio_pcd = "R$ 2000" if i == 1 else "R$ 1000" if i == 2 else "R$ 500"
        print(f"Colocação: {corredor_pcd['colocacao']}, Nome: {corredor_pcd['corredor']}, Idade: {corredor_pcd['idade']}, Categoria: {corredor_pcd['categoria']}, Medalha: {corredor_pcd['medalha']}, Troféu: {corredor_pcd['trofeu']}, Premiação: {premio_pcd} \n")

# Executa a função principal se este arquivo for executado diretamente
if __name__ == "__main__":
    main()