from Trade import Trade


if __name__ == '__main__':
    price_list = [9, 10, 12, 8, 6]
    trade = Trade(closing_prices=price_list)
    profit_method1 = trade.calculate_profit()
    profit_method2 = trade.get_profit()