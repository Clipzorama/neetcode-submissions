class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
        

    def next(self, price: int) -> int:

        self.prices.append(price)
        
        i = len(self.prices) - 1

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if self.stack:
            span = i - self.stack[-1]
        else:
            span = i + 1

        self.stack.append(i)

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)