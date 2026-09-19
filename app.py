imovel = input("Digite um ímovel (opções esperadas: comercial, casa ou apartamento): ")
consumo_mensal_agua = float(input("Digite o seu consumo mensal de água em metros cúbicos (m3) (numero decimal): "))

match imovel:
    case "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    case "apartamento" if consumo_mensal_agua < 10:
        print("Consumo econômico – excelente controle de água!")

    case "apartamento" | "casa" if consumo_mensal_agua <= 25:
        print("Consumo moderado – dentro do padrão residencial.")

    case _:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
