from say_number import say_number

def test_say_number():
    # test cases for 0
    assert say_number(0) == "Zero."

    # test cases for single-digit numbers
    assert say_number(1) == "One."
    assert say_number(5) == "Five."
    assert say_number(9) == "Nine."

    # test cases for double-digit numbers
    assert say_number(11) == "Eleven."
    assert say_number(22) == "Twenty Two."
    assert say_number(35) == "Thirty Five."
    assert say_number(99) == "Ninety Nine."

    # test cases for larger numbers
    assert say_number(100) == "One Hundred."
    assert say_number(123) == "One Hundred and Twenty Three."
    assert say_number(1000) == "One Thousand."
    assert say_number(1043283) == "One Million, Forty Three Thousand, Two Hundred and Eighty Three."
    assert say_number(90376000010012) == "Ninety Trillion, Three Hundred and Seventy Six Billion, Ten Thousand and Twelve."

if __name__ == "__main__":
  test_say_number()