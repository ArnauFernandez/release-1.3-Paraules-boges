import os
from crazywords import *
import logging
input_dir = "./entrada"
output_dir = "./sortida"
log_dir = "./log"

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace(".txt", "Bojes.txt"))
        log_file = os.path.join(log_dir, "error.log")

#pruebas
    logFile = log_file
    logFormat = '%(asctime)s %(levelname)s %(message)s'
    logLevel = logging.DEBUG
    logMode = 'a'
    logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode)

    try:
        input_file = open(input_file, mode="rt", encoding='utf-8')
        output_file = open(output_file, mode="wt", encoding='utf-8')
        linea = input_file.readline()
        if linea == "":
            logging.warning("El archivo de entrada esta vacio")
        while linea != "":
            lista_paraules = linea.split(" ")
            for paraula in lista_paraules:
                paraula_nova = crazywords(paraula)
                output_file.write(paraula_nova + " ")
            output_file.write("\n")
            linea = input_file.readline()
        output_file.close()
    except:
        logging.error("Error al abrir los archivos")