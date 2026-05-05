from abc import ABC, abstractmethod

# Interface base para o cálculo de pagamento
class CalculadoraPagamento(ABC):
    @abstractmethod
    def calcular_bruto_semanal(self, dados: dict) -> float:
        pass

# Estratégia de cálculo para CLT
class CalculadoraCLT(CalculadoraPagamento):
    def __init__(self, salario_mensal: float, jornada_semanal: int = 44):
        self.salario_mensal = salario_mensal
        self.jornada_semanal = jornada_semanal
        self.horas_mensais_padrao = 220  # Base legal para 44h/semana

    def calcular_bruto_semanal(self, dados: dict) -> float:
        # 1. Encontrar o valor da hora de trabalho
        valor_hora = self.salario_mensal / self.horas_mensais_padrao
        
        # 2. Valor proporcional da semana regular (44h)
        # (Isso provisiona a base do salário para o financeiro na semana)
        valor_semana_regular = valor_hora * self.jornada_semanal
        
        # 3. Cálculo das horas extras com 50% de adicional
        horas_extras = dados.get("horas_extras", 0)
        valor_hora_extra = valor_hora * 1.5
        total_extras = horas_extras * valor_hora_extra
        
        # Nota: Em um sistema de produção real, o DSR (Descanso Semanal Remunerado) 
        # sobre as horas extras também seria calculado aqui.
        return valor_semana_regular + total_extras

# Estratégia de cálculo para PJ
class CalculadoraPJ(CalculadoraPagamento):
    def __init__(self, valor_hora: float):
        self.valor_hora = valor_hora

    def calcular_bruto_semanal(self, dados: dict) -> float:
        horas_trabalhadas = dados.get("horas_trabalhadas", 0)
        return self.valor_hora * horas_trabalhadas

# Estratégia de cálculo para Diarista
class CalculadoraDiarista(CalculadoraPagamento):
    def __init__(self, valor_dia: float):
        self.valor_dia = valor_dia

    def calcular_bruto_semanal(self, dados: dict) -> float:
        dias_trabalhados = dados.get("dias_trabalhados", 0)
        return self.valor_dia * dias_trabalhados

# ==========================================
# Execução do Desafio e Teste dos Cenários
# ==========================================
def processar_folha_semanal():
    # Parâmetros contratuais
    joao = CalculadoraCLT(salario_mensal=2200.00)
    maria = CalculadoraPJ(valor_hora=50.00)
    jose = CalculadoraDiarista(valor_dia=150.00)

    # Dados recebidos do sistema de ponto na semana
    ponto_joao = {"horas_extras": 5}
    ponto_maria = {"horas_trabalhadas": 40}
    ponto_jose = {"dias_trabalhados": 3}

    # Processamento e Saída
    print("--- FECHAMENTO FINANCEIRO SEMANAL ---")
    print(f"João (CLT): R$ {joao.calcular_bruto_semanal(ponto_joao):.2f}")
    print(f"Maria (PJ): R$ {maria.calcular_bruto_semanal(ponto_maria):.2f}")
    print(f"José (Diarista): R$ {jose.calcular_bruto_semanal(ponto_jose):.2f}")

if __name__ == "__main__":
    processar_folha_semanal()