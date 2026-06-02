from sqlalchemy import create_engine

cadena_base_datos = 'postgresql+psycopg2://user:password@localhost:5434/postgres' # Cadena de postgres
#cadena_base_datos = 'mysql+pymysql://root:rootpassword@localhost:3308/universidad' #Cadena de mariadb

# cadena_base_datos = 'sqlite:///universidad.db'  #Cadena de sqlite

engine = create_engine(cadena_base_datos)
