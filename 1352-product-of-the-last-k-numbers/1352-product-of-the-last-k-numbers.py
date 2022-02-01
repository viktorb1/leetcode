class ProductOfNumbers:

    def __init__(self):
        self.aggProd = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.aggProd = [1]
        else:
            self.aggProd.append(self.aggProd[-1]*num)

    def getProduct(self, k: int) -> int:
        if len(self.aggProd) <= k:
            return 0
        elif len(self.aggProd) > k:
            return self.aggProd[-1] // self.aggProd[-1-k]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)