import re
import csv

# Ruta completa del archivo de entrada
input_file = r"task3.txt"
# Ruta completa del archivo de salida
output_file = r"output_task3.csv"

# Expresiones regulares para extraer datos
regex_id = r'\b\d+\b'  # IDs: números enteros
regex_email = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'  # Correos electrónicos
regex_date = r'\b\d{4}-\d{2}-\d{2}\b'  # Fechas en formato YYYY-MM-DD
regex_url = r'\bhttps?://[^\s]+\b'  # URLs que empiezan con http o https
regex_surname = r'\b[A-Z][a-zA-Z]+\b'  # Palabras que parecen apellidos (primera letra mayúscula)

# Leer el contenido del archivo
with open(input_file, "r", encoding="utf-8") as file:
    data = file.read()

# Extraer datos usando las expresiones regulares
ids = re.findall(regex_id, data)
emails = re.findall(regex_email, data)
dates = re.findall(regex_date, data)
urls = re.findall(regex_url, data)

# Extraer apellidos eliminando otros datos ya encontrados
remaining_data = re.sub(f"{regex_id}|{regex_email}|{regex_date}|{regex_url}", "", data)
surnames = re.findall(regex_surname, remaining_data)

# Asegurar que todas las listas tengan la misma longitud
min_length = min(len(ids), len(surnames), len(emails), len(dates), len(urls))
ids = ids[:min_length]
surnames = surnames[:min_length]
emails = emails[:min_length]
dates = dates[:min_length]
urls = urls[:min_length]

# Guardar los datos en un archivo CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Last Name", "Email", "Registration Date", "Website"])
    for i in range(min_length):
        writer.writerow([ids[i], surnames[i], emails[i], dates[i], urls[i]])

print(f"Data processed and saved to '{output_file}' successfully.")





