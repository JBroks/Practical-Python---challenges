def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)

def test_between(value,lower_limit,upper_limit):
    assert value <= upper_limit and value >= lower_limit, "{0} is not between {1} and {2}".format(value, lower_limit, upper_limit)


# Test to fail the `test_not_equal` function
#test_not_equal(count_numbers([1,2,3]), False)

# Test to fail the `test_are_equal` function
#test_are_equal(number_of_evens([1,2,3,4,5]), 2)

# Test to fail the `test_not_in` function
#test_not_in([0,1,2,3,4], number_of_evens([1,2,3]))

# Test to fail the `test_between` function
#test_between(1,2,4)

