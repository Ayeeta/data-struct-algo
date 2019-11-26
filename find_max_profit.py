def min_max(arr):
    if len(arr) == 0:
        return 0
    else:
        min_val = min(arr)
        max_val = max(arr[arr.index(min_val):])
        if min_val < max_val:
            return max_val - min_val
        else:
            return 0


def maxProfit(self, prices):
        min=6666666
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            elif maxprofit<prices[i]-min:
                maxprofit=prices[i]-min
        return maxprofit

print(min_max([2,4,1]))