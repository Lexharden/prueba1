# import csv
#
#
# def abrir_archivo():
#     # Abre el archivo CSV en modo lectura
#     with open('data_prueba_tecnica.csv', 'r+') as f:
#         # Crea un objeto CSV reader
#         reader = csv.reader(f)
#         # Crea una lista para almacenar las filas no vacías
#         filtered_rows = []
#         # Itera sobre las filas del archivo CSV
#         for row in reader:
#             # Verifica si la fila tiene al menos un elemento
#             if row:
#                 # Si la fila no está vacía, agrégala a la lista de filas filtradas
#                 filtered_rows.append(row)
#
#         # Muestra las filas filtradas
#         print(filtered_rows)
#
#
# def modificar_archivo():
#     # Abre el archivo CSV en modo escritura
#     with open('archivo_mejorado.csv', 'w', newline='') as f:
#         # Crea un objeto CSV writer
#         writer = csv.writer(f)
#         # Itera sobre las filas filtradas y las escribe en el archivo CSV
#         for row in abrir_archivo():
#             writer.writerow(row)
#         f.close()
