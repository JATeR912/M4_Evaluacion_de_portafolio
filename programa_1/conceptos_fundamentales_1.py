# Conversor de monedas (CLP a USD, EUR, GBP, YEN, CNY, MXN, ARS, PEN)

input_valor = int(input("Ingrese el valor a convertir (CLP): "))

if input_valor < 0:
    print("Por favor ingrese un valor positivo.")
elif input_valor >= 1:
    unidad_destino = input("Ingrese la unidad de destino (USD, EUR, GBP, YEN, CNY, MXN, ARS, PEN): ").lower()
    
    if unidad_destino == "usd":
        valor_convertido = input_valor * 0.00104
    elif unidad_destino == "eur":
        valor_convertido = input_valor * 0.00089
    elif unidad_destino == "gbp":
        valor_convertido = input_valor * 0.00078
    elif unidad_destino == "yen":
        valor_convertido = input_valor * 0.15194
    elif unidad_destino == "cny":
        valor_convertido = input_valor * 0.00750
    elif unidad_destino == "mxn":
        valor_convertido = input_valor * 0.02035
    elif unidad_destino == "ars":
        valor_convertido = input_valor * 1.421
    elif unidad_destino == "pen":
        valor_convertido = input_valor * 0.00388
    else:
        print("Por favor ingrese una unidad válida.")
        exit()
    
    print(f"{input_valor} CLP son: {valor_convertido:.2f} {unidad_destino.upper()}")
else:
    print("Por favor ingrese un valor valido.")