class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b=prices[0]
        s=prices[0]
        for i in range(0, len(prices)):
            if prices[i]< b:
                b=prices[i]
                s=prices[i]
                for j in range(i+1, len(prices)):
                    if prices[j]>s:
                        s=prices[j]
        return s-b