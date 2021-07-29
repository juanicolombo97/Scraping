#Imports
from variables_imports import *

# Implementacion


# Funcion que se encarga de iterar sobre las tablas de expediente y appendear los que cumplen la condicion 8,  a una lista de listas.
def iteracion_tabla():
    
    # Iteramos sobre los expedientes hasta obtener 100
    contador = 0
    while (contador < CANTIDAD_EXPEDIENTES): 
        expedientes = driver.find_elements_by_xpath(TABLA_EXPEDIENTES_ID) 
        for x in range(0, len(expedientes)-1):
            expediente_nuevo = []
            situaciones = driver.find_elements_by_xpath(SITUACION_ID)
            ultima_actividades = driver.find_elements_by_xpath(ULTIMA_ACT_ID)
            botones_ojo = driver.find_elements_by_xpath(BOTON_OJO_ID)  
            try:
                situacion = situaciones[x].text
            except:
                print('Error')
                continue
            ult_act = pd.to_datetime(ultima_actividades[x].text)
            if ((situacion in SITUCAION_REQUERIDA) and  (FECHA_LIMITE < ult_act) and (contador < CANTIDAD_EXPEDIENTES)):
                try:
                    boton_ojo = botones_ojo[x]
                    boton_ojo.click()
                    time.sleep(1)
                    expediente_nuevo.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[2]/div/div/fieldset/div/div[1]/div/div/div[2]/span').text)
                    expediente_nuevo.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[2]/div/div/fieldset/div/div[2]/div/div/div[2]/span').text)
                    expediente_nuevo.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[2]/div/div/fieldset/div/div[4]/div/div/div[2]/span').text)
                    expediente_nuevo.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[2]/div/div/fieldset/div/div[5]/div/div/div[2]/span').text)
                    tab_intervinientes = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[3]/div/div[1]/table/tbody/tr/td[6]')
                    tab_intervinientes.click()
                    time.sleep(1)
                    expediente_nuevo.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[3]/div/div[4]/div/div/table/tbody[1]/tr/td[2]/span[2]').text)
                    expediente_nuevo.append(driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[3]/div/div[4]/div/div/table/tbody[3]/tr/td[2]/span[2]').text)
                    
                    EXPEDIENTES_FINALES.append(expediente_nuevo)
                    boton_volver = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[1]/div/div/a')
                    boton_volver.click()
                    contador = contador + 1
                    time.sleep(5)
                    print("Expediente apendado.")
                except:
                    print("Error")
                    continue      
        print(contador)
        if (contador >= CANTIDAD_EXPEDIENTES):
            break
        time.sleep(2)
        boton_siguiente = driver.find_element_by_id(BOTON_SIGUIENTE_ID)
        boton_siguiente.click()
        time.sleep(TIEMPO_ESPERA_NUEVOS_EXPEDIENTES)

# Funcion que se mueve a la seccion 'Por parte', ingresa la jurisdiccion 'CIV' y la parte 'SOCIEDAD'. Espera
# que el usuario realize la captcha y luego procese a presionar el boton Consultar para pasar a la ventana de la tabla.
def moverse_a_pagina_tabla_expediente():
    # Nos movemos a buscar por parte (id: formPublica:porParte:header:inactive)
    busqueda_por_parte = driver.find_element_by_id(BUSQUEDA_ID)
    busqueda_por_parte.click()
    time.sleep(TIEMPO_ESPERA_NUEVA_ACCION)

    # Seleccionamos Jurisdiccion ( "CIV – Cámara Nación de Apelaciones en lo Civil")
    jurisdiccion = driver.find_element_by_id(SELECT_ID)
    jurisdiccion_elegida = Select(jurisdiccion)
    jurisdiccion_elegida.select_by_visible_text(JURISDICCION_ELEGIDA)

    # Escribimos en PARTE "SOCIEDAD"
    parte = driver.find_element_by_name(PARTE_ID)
    parte.send_keys(VALOR_BUSQUEDA)

    # Esperamos un tiempo para la CAPTCHA
    time.sleep(TIEMPO_ESPERA_CAPTCHA)

    # Clickeamos boton consultar
    boton_consultar = driver.find_element_by_id(BOTON_ID)
    boton_consultar.click()

  

# Funcion Main , maneja el programa.
def main():
    
    # Cargo pagina
    driver.get(WEB_PAGE)

    # Abro Excel
    if os.path.exists('archivo_expedientes.xlsx'):
        ARCHIVO_EXCEL = load_workbook('archivo_expedientes.xlsx')
    else:
        ARCHIVO_EXCEL = Workbook()
        EXPEDIENTES_FINALES.append(["Expediente", "Jurisdicción", "Situación Actual", "Carátula", "Actores", "Demandados"])     
    ARCHIVO_EXPEDIENTES = ARCHIVO_EXCEL.active

    moverse_a_pagina_tabla_expediente()
    iteracion_tabla()
    
    # Guardo los expedientes en el archivo, lo guardo y cierro la pagina web.
    for expediente in EXPEDIENTES_FINALES:
        ARCHIVO_EXPEDIENTES.append(expediente)
    ARCHIVO_EXPEDIENTES.save("archivo_expedientes.xlsx")
    driver.quit()
    

main()

