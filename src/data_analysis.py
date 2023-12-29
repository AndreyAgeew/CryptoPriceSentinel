import pandas as pd
from sklearn.linear_model import LinearRegression
from database_manager import get_historical_data


def perform_regression_analysis():
    data = get_historical_data()
    df = pd.DataFrame(data, columns=['timestamp', 'eth_price', 'btc_price'])

    # Преобразование данных для анализа
    df['eth_return'] = df['eth_price'].pct_change()
    df['btc_return'] = df['btc_price'].pct_change()
    df.dropna(inplace=True)

    # Регрессионный анализ
    X = df[['btc_return']]  # Независимая переменная
    y = df['eth_return']  # Зависимая переменная
    model = LinearRegression().fit(X, y)

    # Многострочный вывод
    print(f"""
    Результаты регрессионного анализа:
    Коэффициент (Coefficients): {model.coef_[0]:.4f}
    Это значение показывает, на сколько процентов изменяется цена ETH (eth_return),
    при изменении цены BTC (btc_return) на один процент.
    Положительный коэффициент указывает на прямую зависимость между ценами ETH и BTC.
    Отрицательный коэффициент указывает на обратную зависимость.

    Перехват (Intercept): {model.intercept_:.4f}
    Перехват (или точка пересечения с осью Y) показывает предсказанное значение изменения цены ETH (eth_return),
    когда изменение цены BTC (btc_return) равно нулю. В реальности это значение имеет ограниченную интерпретацию,
    поскольку цены на криптовалюту редко остаются статичными.
    """)