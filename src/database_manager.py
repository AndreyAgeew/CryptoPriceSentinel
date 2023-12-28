import psycopg2
from datetime import datetime

from src.config import DB_HOST, DB_NAME, DB_USER, DB_PASS

# Database configuration
db_config = {
    'host': DB_HOST,
    'database': DB_NAME,
    'user': DB_USER,
    'password': DB_PASS
}


def connect_to_db():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None


def insert_prices_to_db(eth_price, btc_price):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO price_data (timestamp, eth_price, btc_price) VALUES (%s, %s, %s)"
            timestamp = datetime.now()
            cursor.execute(query, (timestamp, eth_price, btc_price))
            conn.commit()
        except Exception as e:
            print(f"Error inserting data into PostgreSQL database: {e}")
        finally:
            conn.close()