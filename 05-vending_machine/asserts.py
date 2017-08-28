from byotest import *
from vending_machine import *

test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(3),[2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])

print("All tests pass")