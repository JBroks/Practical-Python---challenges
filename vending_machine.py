from byotest import *

euro_coins = {1: 20, 2: 20, 5: 20, 10: 20, 20: 20, 50: 20, 100: 20}
usd_coins = {1: 20, 5: 20, 10: 20, 25: 20, 50: 20, 100: 20}

def get_change(amount, coins = euro_coins):
    change = []
    for denomination in sorted(coins.keys(), reverse=True):
        while denomination <= amount and coins[denomination] > 0:
            amount -= denomination
            change.append(denomination)
    if amount != 0:
        raise Exception("Insufficient coins to give change.")
    return change
 
test_are_equal(get_change(0),[])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(9), [5,2,2])
test_are_equal(get_change(35, usd_coins), [25,10])


print("All test pass!")