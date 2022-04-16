#PROGRAMA PARA MEDIR O ÍNDICE DE MASSA CORPORAL(IMC)
def imc(Peso,Altura):
    try:
        Peso = float(Peso)
        Altura = float(Altura)
    except ValueError:
        return "Entrada inválida. As entradas devem ser numéricas"

    if ( (1.0 > Peso or Peso > 600.0) or (0.40 > Altura or Altura > 3) ):
        return "Entrada Inválida. Verifique os valores inseridos"
#Calculo do IMC
    imc = Peso / Altura**2

    if (imc < 18.5):
        return "Abaixo do peso"
    elif (18.5 <= imc < 25):
        return "Peso normal"
    elif (25 <= imc < 30):
        return "Acima do peso"
    elif (30 <= imc < 40):
        return "Acima do Peso(Obesidade)"
    elif (imc >= 40):
        return  "Acima do peso(Obesiidade grave)"