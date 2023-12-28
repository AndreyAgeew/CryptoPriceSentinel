import time
from data_collector import collect_data
from price_alert import check_price_movement


def main():
    while True:
        collect_data()
        check_price_movement()
        time.sleep(60)  # Ждем 60 секунд перед следующей проверкой


if __name__ == "__main__":
    main()
