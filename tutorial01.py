import pandas as pd
HOLA = "HOLA"
fecha_1 = pd.to_datetime("31/12/2019")
fecha_2 = pd.to_datetime("01/12/2020")

print(fecha_1 < fecha_2)

SITUCAION_REQUERIDA = ["EN DESPACHO", "EN LETRA", "GIRO"]
EXPEDIENTES_FINALES = [["Expediente", "Jurisdicción", "Situación Actual", "Carátula", "Actores", "Demandados"]]
print("EN DESPACHO" in SITUCAION_REQUERIDA)

def main():
    
    EXPEDIENTES_FINALES.append(["HOLA"])
    for x in EXPEDIENTES_FINALES:
        print(x)

main()