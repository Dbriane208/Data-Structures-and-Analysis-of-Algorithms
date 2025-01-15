# time O(nlogn) | space O(1)
def nonConstructibleChange(coins):
    coins.sort()

    currentChage = 0

    for coin in coins:
        if coin > currentChage + 1:
            return currentChage + 1
        currentChage += coin

    return currentChage + 1    