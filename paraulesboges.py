"""
Eric González, Izan Fernandez, Arnau Fernandez.
08/05/2024
M03 UF3
Descripció: Lliurament R3 ParaulesBoges

"""
import os
import logging
from crazywords import crazywords

def setup_logging(log_file, log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', log_level=logging.DEBUG, log_mode='a'):
    logging.basicConfig(level=log_level, format=log_format, filename=log_file, filemode=log_mode)

def process_file(input_file, output_file):
    try:
        try:
            with open(input_file, mode="rt", encoding='utf-8') as input_f, open(output_file, mode="wt", encoding='utf-8') as output_f:
                linea = input_f.readline()
                if not linea:
                    logging.warning(f"El archivo de entrada '{input_file}' está vacío")
                while linea:
                    lista_palabras = linea.split(" ")
                    for palabra in lista_palabras:
                        palabra_nueva = crazywords(palabra)
                        output_f.write(palabra_nueva)
                    linea = input_f.readline()
        except:
            with open(input_file, mode="rt", encoding='latin_1') as input_f, open(output_file, mode="wt", encoding='latin_1') as output_f:
                linea = input_f.readline()
                if not linea:
                    logging.warning(f"El archivo de entrada '{input_file}' está vacío")
                while linea:
                    lista_palabras = linea.split(" ")
                    for palabra in lista_palabras:
                        palabra_nueva = crazywords(
                            palabra)
                        output_f.write(palabra_nueva)
                    linea = input_f.readline()
    except Exception as e:
        logging.error(f"Error al procesar el archivo '{input_file}': {e}")

def main(input_dir, output_dir, log_dir):
    setup_logging(os.path.join(log_dir, "boges.log"))
    logging.info("Inicio del programa.")

    try:
        # Verificar y crear directorio de salida si no existe
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info(f"Directorio de salida creado en: {output_dir}")

        for filename in os.listdir(input_dir):
            if filename.endswith(".txt"):
                input_file = os.path.join(input_dir, filename)
                output_file = os.path.join(output_dir, filename.replace(".txt", "Boges.txt"))
                process_file(input_file, output_file)

        logging.info("Proceso de archivos completado.")

    except Exception as e:
        logging.error(f"Error durante el procesamiento de archivos: {e}")



