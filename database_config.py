import os

def get_database_config():
    host = os.environ.get('POSTGRES_HOST', 'localhost')
    database = os.environ.get('POSTGRES_DB', 'COFFTO_COFFEE_DB')
    user = os.environ.get('POSTGRES_USER', 'postgres')
    password = 'betaTrident1@'
    return {
        'host': host,
        'database': database,
        'user': user,
        'password': password
    }
