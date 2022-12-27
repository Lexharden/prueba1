import psycopg2 as ps
import csv

# Crear la conexión a la base de datos
cnx = ps.connect(
    host='localhost',
    user='postgres',
    password='password',
    database='prueba_tecnica'
)

cursor = cnx.cursor()
# Abre el archivo CSV en modo lectura
with open('data_new.csv', 'r') as f:
    # Crea un objeto CSV reader
    reader = csv.reader(f)
    # Salta la primera fila (la fila de encabezados)
    next(reader)
    query1 = """
    CREATE TABLE cargo (
        id VARCHAR(40) NOT NULL,
        company_name VARCHAR(130) NULL,
        company_id VARCHAR(41) NOT NULL,
        amount DECIMAL(16,2) NOT NULL,
        status CHAR(30) NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NULL
    );
    """
    cursor.execute(query1)
    query = "INSERT INTO cargo (id, company_name, company_id, amount, status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, to_timestamp(%s, 'YYYY-MM-DD'),to_timestamp(%s, 'YYYY-MM-DD'))"
    # Itera sobre las filas del archivo CSV
    # cursor.execute(query1)
    for row in reader:
        print(row)

        cursor.execute(query, row)
        # Realiza el commit para guardar los cambios en la base de datos
        cnx.commit()
        # Cierre la conexión a la base de datos
    cnx.close()
