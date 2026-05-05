# Teste Técnico - Construtora Guimarães
> Sistema de Controle de Ponto e Fechamento Financeiro.

## 📋 Descrição do Projeto
Este projeto apresenta a solução para o desafio técnico de gestão de colaboradores (CLT, PJ e Diaristas). A solução contempla o desenho da arquitetura de dados e a implementação da lógica de cálculo de pagamentos.

---

## 🏗️ Parte 1: Arquitetura e Regras de Negócio

### 1. Modelagem de Dados
Para garantir escalabilidade, a estrutura proposta separa os dados cadastrais das regras contratuais:
* **Tabelas principais:** `Colaborador`, `Contrato` (onde define se é CLT, PJ ou Diarista) e `RegistroPonto`.
* **Benefício:** Permite que um mesmo colaborador tenha históricos de contratos diferentes sem perder a integridade dos dados.

### 2. Fluxo de Caixa (Semanal vs Mensal)
A solução proposta utiliza o conceito de **Provisão Contábil**. 
* Embora o pagamento CLT seja mensal, o sistema gera uma reserva financeira semanal para que o financeiro visualize o custo real da obra em tempo real.

---

## 💻 Parte 2: Desafio de Lógica (Python)

### Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Conceitos:** Programação Orientada a Objetos (POO) e Padrão de Projeto Strategy.

### Como Executar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `solucao.py`.
3. Execute o comando:
   ```bash
   python solucao.py
