from data_collector import collect_data
from price_alert import check_price_movement
from data_analysis import perform_regression_analysis
import time


def main():
    # Выполнение регрессионного анализа
    perform_regression_analysis()

    # Периодический сбор и анализ данных
    while True:
        collect_data()
        check_price_movement()  # передайте модель в функцию оповещения
        time.sleep(60)  # Пауза 60 секунд


if __name__ == "__main__":
    main()
