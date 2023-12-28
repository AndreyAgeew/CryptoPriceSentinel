from database_manager import connect_to_db
from datetime import datetime, timedelta

def check_price_movement():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            SELECT eth_price FROM price_data 
            WHERE timestamp >= %s
            ORDER BY timestamp ASC
            """
            one_hour_ago = datetime.now() - timedelta(hours=1)
            cursor.execute(query, (one_hour_ago,))
            prices = cursor.fetchall()

            if prices:
                start_price = prices[0][0]
                current_price = prices[-1][0]

                if abs((current_price - start_price) / start_price) >= 0.01:
                    print(f"ETH price moved by 1% or more in the last 60 minutes: {current_price}")
        except Exception as e:
            print(f"Error checking price movement: {e}")
        finally:
            conn.close()