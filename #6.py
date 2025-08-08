#6. [Conversor de Temperatura com Faixas de Alerta]]
#Se a temperatura for abaixo de 0°C ou superior a 40°C (após conversão), exibir “⚠️
#Alerta extremo para [localização]”.
#F = (C × 9/5) + 32
#C = (F − 32) × 5/9
#K = C + 273.15

# Conversor de Temperatura com Faixas de Alerta
tipo = input("Escolha o tipo de conversão (C→F, F→C, C→K): ")
temperatura = float(input("Digite a temperatura: "))
localizacao = input("Informe a sua localização: ")
resultado = None
temperatura_convertida_em_celsius = None  # para avaliar se gera alerta

# Conversão com base no tipo escolhido
if tipo == "C→F":
    resultado = (temperatura * 9/5) + 32
    temperatura_convertida_em_celsius = temperatura
    print(f"{temperatura}°C = {resultado:.2f}°F")

elif tipo == "F→C":
    resultado = (temperatura - 32) * 5/9
    temperatura_convertida_em_celsius = resultado
    print(f"{temperatura}°F = {resultado:.2f}°C")

elif tipo == "C→K":
    resultado = temperatura + 273.15
    temperatura_convertida_em_celsius = temperatura
    print(f"{temperatura}°C = {resultado:.2f}K")

else:
    print("Tipo de conversão inválido.")
    exit()

# Alerta climático
if temperatura_convertida_em_celsius < 0 or temperatura_convertida_em_celsius > 40:
    print(f"⚠️ Alerta extremo para {localizacao}")
