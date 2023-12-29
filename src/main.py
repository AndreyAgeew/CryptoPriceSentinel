from data_collector import collect_data
from price_alert import check_price_movement
from data_analysis import perform_regression_analysis
import time


def main():
    # Получение модели регрессии и последнего изменения цены BTC
    regression_model = perform_regression_analysis()

    while True:
        collect_data()
        check_price_movement(regression_model)  # Передаем модель
        time.sleep(60)  # Ждем 60 секунд перед следующей проверкой


if __name__ == "__main__":
    main()
