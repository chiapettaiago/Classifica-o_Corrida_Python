# 🏃‍♂️ Sistema de Classificação para Maratona Cidade Verde 2025

![Maratona](https://img.shields.io/badge/Evento-Maratona%20Cidade%20Verde-brightgreen)
![Python](https://img.shields.io/badge/Linguagem-Python-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📋 Descrição do Projeto

Este projeto simula os resultados de uma maratona chamada "Cidade Verde 2025", gerando aleatoriamente os participantes, suas colocações e organizando os resultados em rankings. O sistema inclui tanto uma classificação geral quanto uma categoria especial para PCD (Pessoas com Deficiência).

## ✨ Funcionalidades

- **Geração Aleatória de Participantes**: Nomes, idades e categorias são gerados automaticamente.
- **Classificação por Ranking**: Os participantes são classificados de 1º ao 5º lugar.
- **Premiações Diferenciadas**: Valores específicos para o ranking geral e para a categoria PCD.
- **Categorias PCD**: Inclusão de categorias específicas para atletas com deficiência.

## 🏆 Sistema de Premiação

### Ranking Principal
| Colocação | Medalha | Troféu | Premiação |
|-----------|---------|--------|-----------|
| 1º Lugar  | Ouro    | Sim    | R$ 10.000 |
| 2º Lugar  | Prata   | Sim    | R$ 5.000  |
| 3º Lugar  | Bronze  | Sim    | R$ 3.000  |
| 4º Lugar  | -       | Sim    | R$ 1.500  |
| 5º Lugar  | -       | Sim    | R$ 1.000  |

### Ranking PCD
| Colocação | Medalha | Troféu | Premiação |
|-----------|---------|--------|-----------|
| 1º Lugar  | Ouro    | Sim    | R$ 2.000  |
| 2º Lugar  | Prata   | Sim    | R$ 1.000  |
| 3º Lugar  | Bronze  | Sim    | R$ 500    |

## 🧩 Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **Classes para Geração de Dados**:
  - `GeradorNomes`: Gera nomes aleatórios para os participantes
  - `GeradorIdade`: Gera idades aleatórias dentro da faixa permitida (18-60 anos)
  - `GeradorCategoria`: Gera categorias PCD para os participantes
  - `Colocacao`: Gerencia as colocações possíveis

- **Função Principal**: Coordena todo o fluxo do sistema, desde a criação dos participantes até a exibição dos resultados.

## 📊 Categorias PCD Incluídas

- PCD - Deficiência Física
- PCD - Deficiência Visual
- PCD - Amputados

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Módulo Random para geração de dados aleatórios

## ⚙️ Como Executar

1. Certifique-se de ter o Python instalado em seu computador
2. Clone este repositório
3. Execute o seguinte comando:

```bash
python app.py
```

## 📝 Exemplo de Saída

```
 Maratona Cidade Verde 2025 

 Ranking Principal: 

Colocação: 1º Lugar, Nome: João, Idade: 25, Medalha: Ouro, Troféu: Sim, Premiação: R$ 10000 

Colocação: 2º Lugar, Nome: Maria, Idade: 34, Medalha: Prata, Troféu: Sim, Premiação: R$ 5000 

Colocação: 3º Lugar, Nome: Lucas, Idade: 42, Medalha: Bronze, Troféu: Sim, Premiação: R$ 3000 

Colocação: 4º Lugar, Nome: Ana, Idade: 29, Medalha: -, Troféu: Sim, Premiação: R$ 1500 

Colocação: 5º Lugar, Nome: Rafael, Idade: 36, Medalha: -, Troféu: Sim, Premiação: R$ 1000 

 Ranking da Categoria PCD: 

Colocação: 1º Lugar, Nome: João, Idade: 25, Categoria: PCD - Deficiência Física, Medalha: Ouro, Troféu: Sim, Premiação: R$ 2000 

Colocação: 2º Lugar, Nome: Maria, Idade: 34, Categoria: PCD - Deficiência Visual, Medalha: Prata, Troféu: Sim, Premiação: R$ 1000 

Colocação: 3º Lugar, Nome: Lucas, Idade: 42, Categoria: PCD - Amputados, Medalha: Bronze, Troféu: Sim, Premiação: R$ 500 
```

## 👨‍🎓 Sobre o Projeto

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de Programação em Python. O objetivo foi demonstrar a aplicação de conceitos de Programação Orientada a Objetos, como classes, herança e encapsulamento, além de manipulação de estruturas de dados.

---

© 2025 - Maratona Cidade Verde | Desenvolvido para fins acadêmicos
