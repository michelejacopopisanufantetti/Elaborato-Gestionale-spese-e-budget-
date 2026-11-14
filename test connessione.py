import psycopg2

# Configurazione credenziali database
DB_CONFIG = {
    "dbname": "gestione_spese",
    "user": "postgres",
    "password": "1234",  # Inserisci la password impostata all'installazione
    "host": "localhost",
    "port": "5432"
}

def test_connessione():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connessione a PostgreSQL stabilita con successo!")
        conn.close()
    except Exception as e:
        print(f"Errore di connessione: {e}")

if __name__ == "__main__":
    test_connessione()
