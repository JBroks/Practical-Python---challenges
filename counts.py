def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("$%^A") == 1, "One upper with special characters"
assert count_upper_case("Abraham John") == 2, "Two upper cases"
assert count_upper_case("ADSNSNSJ ANANNA ANNNaaaa") == 18, "Multiple upper cases"
assert count_upper_case("assjahsdkjshfjsh dfkjshdfjds dfjhsfk aaaA") == 1, "Last upper case"
assert count_upper_case("sgshjfgsfsdjfgjsd") == 0, "multiple lower cases"

print("All the tests passed")