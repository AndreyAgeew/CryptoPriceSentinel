from database_manager import connect_to_db
from datetime import datetime, timedelta

def check_price_movement():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            SELECT eth_price, btc_price FROM price_data 
            WHERE timestamp >= %s
            ORDER BY timestamp ASC
            """
            one_hour_ago = datetime.now() - timedelta(hours=1)
            cursor.execute(query, (one_hour_ago,))
            records = cursor.fetchall()

            if records:
                start_eth_price, start_btc_price = records[0]
                end_eth_price, end_btc_price = records[-1]

                eth_change = (end_eth_price - start_eth_price) / start_eth_price
                btc_change = (end_btc_price - start_btc_price) / start_btc_price

                # Проверяем изменение цены ETH по отношению к BTC
                if abs(eth_change - btc_change) >= 0.01:
                    print(f"Significant independent movement in ETH price detected: {end_eth_price}")
        except Exception as e:
            print(f"Error checking price movement: {e}")
        finally:
            conn.close()