# Teste Técnico - Grupo Guimarães
> Sistema de Controle de Ponto e Fechamento Financeiro.

##  Descrição do Projeto
Este projeto apresenta a solução para o desafio técnico de gestão de colaboradores (CLT, PJ e Diaristas). A solução contempla o desenho da arquitetura de dados e a implementação da lógica de cálculo de pagamentos.

---

# PARTE 1 – Arquitetura e Regras de Negócio

### 1. Estruturação do Banco de Dados
Para suportar múltiplas modalidades de contratação sem engessar o sistema, a melhor abordagem é normalizar o banco de dados separando os dados do indivíduo dos dados do contrato e das regras de negócio. A estrutura ideal envolveria as seguintes tabelas principais:

*   **Colaborador**: Armazena os dados pessoais estáticos (ID, Nome, CPF/CNPJ, Contato).
*   **Contrato**: Relaciona-se com o colaborador (1:N, pois um diarista hoje pode virar CLT amanhã). Campos: ID, Colaborador_ID, Modalidade (ENUM: CLT, PJ, DIARISTA), Valor_Base, Tipo_Valor (Hora, Dia, Mês), Data_Inicio, Status_Ativo.
*   **RegistroPonto**: Grava os eventos brutos. Campos: ID, Contrato_ID, Data_Hora_Entrada, Data_Hora_Saida.
*   **FechamentoSemanal**: Consolida os dados para o financeiro. Campos: ID, Contrato_ID, Semana_Referencia, Horas_Trabalhadas, Dias_Trabalhados, Horas_Extras, Valor_Bruto, Status_Pagamento.

Essa arquitetura permite que o motor de cálculo (na aplicação) busque a "Modalidade" no Contrato e aplique a regra matemática correspondente sobre os apontamentos da tabela RegistroPonto.

### 2. Fluxo de Caixa Semanal x Ciclo de Folha CLT Mensal 
Para conciliar o fechamento semanal do financeiro com a folha mensal da CLT, o sistema deve utilizar o conceito de Provisão Contábil vs. Contas a Pagar efetivo.

*   **PJ e Diaristas**: O fechamento da semana gera um título de Contas a Pagar real e imediato, pois o fato gerador (trabalho) e o vencimento (fim da semana) coincidem.
*   **CLT**: O fechamento semanal consolida as horas normais e extras daquela semana e gera uma Provisão de Saída no fluxo de caixa do financeiro. O dinheiro não sai da conta do banco naquela semana, mas o sistema financeiro já reserva (compromete) aquele montante.

No momento do pagamento do Adiantamento (dia 20) e do Pagamento Final (5º dia útil), o sistema converte essas provisões semanais acumuladas no mês em um único título de Contas a Pagar efetivo. Isso garante que o financeiro tenha visibilidade do custo semanal sem ferir a legislação trabalhista.

---

# PARTE 2 – Desafio de Lógica (Código em Python)

Para o desenvolvimento deste código, utilizei o **Padrão de Projeto Strategy (Polimorfismo)**. Isso garante que o sistema siga o princípio **Aberto/Fechado (SOLID)**: se a construtora criar uma nova modalidade de contratação (ex: Estagiário), basta criar uma nova classe sem alterar a lógica existente.

Para o colaborador CLT, a lógica adota o padrão de mercado de divisão por 220 horas mensais (para jornadas de 44h semanais) para encontrar o valor da hora e, em seguida, calcula a fração da semana regular somada às horas extras.


### Modelagem de Dados
Para garantir escalabilidade, a estrutura proposta separa os dados cadastrais das regras contratuais:
* **Tabelas principais:** `Colaborador`, `Contrato` (onde define se é CLT, PJ ou Diarista) e `RegistroPonto`.
* **Benefício:** Permite que um mesmo colaborador tenha históricos de contratos diferentes sem perder a integridade dos dados.

### Fluxo de Caixa (Semanal vs Mensal)
A solução proposta utiliza o conceito de **Provisão Contábil**. 
* Embora o pagamento CLT seja mensal, o sistema gera uma reserva financeira semanal para que o financeiro visualize o custo real da obra em tempo real.

### Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Conceitos:** Programação Orientada a Objetos (POO) e Padrão de Projeto Strategy.

### Como Executar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `desafio.py`.
3. Execute o comando:
   ```bash
   python desafio.py
