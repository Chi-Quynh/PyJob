import psycopg2
from .config import load_config  # Assuming load_config() is a function that loads your configuration

def connect(config):
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print("Connection success")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print("Connection error:", error)
        return None

if __name__ == '__main__':
    # Load the config first, ensure it returns a dictionary
    config = load_config()

    if config:
        # Pass the loaded config to the connect function
        connect(config)
    else:
        print("Failed to load configuration.")
