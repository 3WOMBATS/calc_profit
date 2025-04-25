

class Trade:
    """
    Given a list of prices, return the maximum profit, given one buy and one sell and buy before sell
    Public Attributes:
        prices (list, array, series): prices given to calculate profit.
        diff (list): All possible price differences.

    Public Methods:
        all_price_diff(): calculate and compile all possible price differential compos.
        calculate_profit(): return the maximum profit out of all compos.
        get_profit(): A more concise way to achieve the same goal.
    """
    def __init__(self, closing_prices: list) -> None:
        self.prices = closing_prices
        self.diff = list()

    def all_price_diff(self) -> None:
        """Calculate the difference between Nth price and the prior prices"""
        if not self.prices:
            raise ValueError("Missing necessary input prices")

        for i in range(len(self.prices)):
            sell_price = self.prices[i]
            for j in range(i):
                self.diff.append(sell_price-self.prices[j])

    def calculate_profit(self) -> float | int:
        """
        Returns:
            the max price differential from all pairs or 0
        """
        self.all_price_diff()
        if max(self.diff) > 0:
            return max(self.diff)
        else:
            return 0

    def get_profit(self) -> int | float:
        """
        Returns:
            maximum profit in a more concise way
        """
        buy_price = self.prices[0]
        max_profit = 0

        for price in self.prices[1:]:
            profit = price - buy_price
            max_profit = max(max_profit, profit)
            buy_price = min(buy_price, price)
        return max_profit












