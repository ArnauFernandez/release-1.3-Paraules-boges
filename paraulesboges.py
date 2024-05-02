import os
import logging
from crazywords import crazywords  # Asumiendo que crazywords es una función importada desde un módulo llamado 'crazywords'

def setup_logging(log_file, log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', log_level=logging.DEBUG, log_mode='a'):
    """Configura el sistema de registro (logging)."""
    logging.basicConfig(level=log_level, format=log_format, filename=log_file, filemode=log_mode)

def process_file(input_file, output_file):
    """Procesa el archivo de entrada y escribe el resultado en el archivo de salida."""
    try:
        with open(input_file, mode="rt", encoding='utf-8') as input_f, open(output_file, mode="wt", encoding='utf-8') as output_f:
            linea = input_f.readline()
            if not linea:
                logging.warning("El archivo de entrada está vacío")
            while linea:
                lista_palabras = linea.split(" ")
                for palabra in lista_palabras:
                    palabra_nueva = crazywords(palabra)  # Suponiendo que crazywords es una función que realiza alguna transformación en las palabras
                    output_f.write(palabra_nueva + "\n")  # Agregamos una línea después de cada palabra
                linea = input_f.readline()
            output_f.write("\n")  # Agregamos una línea al final del archivo
    except Exception as e:
        logging.error(f"Error al procesar el archivo: {e}")

def main(input_dir, output_dir, log_dir):
    """Función principal que procesa todos los archivos de texto en el directorio de entrada."""
    setup_logging(os.path.join(log_dir, "boges.log"))
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace(".txt", "Boges.txt"))
            process_file(input_file, output_file)

if __name__ == "__main__":
    input_dir = "entrada"
    output_dir = "sortida"
    log_dir = "log"
    main(input_dir, output_dir, log_dir)
