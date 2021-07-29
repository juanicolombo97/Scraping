# Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
from openpyxl import load_workbook
import os
import pandas as pd
import time

# Config Inicial
WEB_PAGE = "http://scw.pjn.gov.ar/scw/home.seam"
BUSQUEDA_ID = "formPublica:porParte:header:inactive"
VALOR_BUSQUEDA = "SOCIEDAD"
SELECT_ID = "formPublica:camaraPartes"
JURISDICCION_ELEGIDA = "CIV - Cámara Nacional de Apelaciones en lo Civil"
PARTE_ID = "formPublica:nomIntervParte"
BOTON_ID = "formPublica:buscarPorParteButton"
BOTON_SIGUIENTE_ID = "j_idt119:j_idt200:j_idt207"
TABLA_EXPEDIENTES_ID = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/form/table/tbody/tr/td[1]'
SITUACION_ID = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/form/table/tbody/tr/td[4]'
ULTIMA_ACT_ID = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/form/table/tbody/tr/td[5]'
BOTON_OJO_ID = "/html/body/div[1]/div[2]/div[1]/div[2]/div/div/div/form/table/tbody/tr/td[6]/a"
TIEMPO_ESPERA_CAPTCHA = 60
TIEMPO_ESPERA_NUEVA_ACCION = 2
TIEMPO_ESPERA_NUEVOS_EXPEDIENTES = 60
CANTIDAD_EXPEDIENTES  = 100
SITUCAION_REQUERIDA = ["EN DESPACHO", "EN LETRA", "GIRO"]
EXPEDIENTES_FINALES = []
FECHA_LIMITE = pd.to_datetime("31/12/2019")
ARCHIVO_EXCEL = None
ARCHIVO_EXPEDIENTES = None

driver = webdriver.Chrome(ChromeDriverManager().install())
