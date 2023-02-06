def say_number(num):
    if num == 0:
        return "Zero."

    # list of number words
    words = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
        19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
        90: 'Ninety'
    }

    # list of scales
    scales = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    # reverse the number to make it easier to extract groups of three
    num_str = str(num)[::-1]

    # split the number into groups of three
    groups = [num_str[i:i+3] for i in range(0, len(num_str), 3)][::-1]

    # initialize the result
    result = []

    for i, group in enumerate(groups):
        # convert the group to an integer
        group = int(group)

        if group == 0:
            continue

        # split the group into hundreds, tens, and ones
        ones = group % 10
        group = group // 10
        tens = group % 10
        group = group // 10
        hundreds = group % 10

        # add the word for the hundreds place
        if hundreds > 0:
            result.append(words[hundreds] + ' Hundred')

        # add the word for the tens place
        if tens > 1:
            result.append(words[tens * 10])
            if ones > 0:
                result.append(words[ones])
        elif tens == 1:
            result.append(words[tens * 10 + ones])
            ones = 0

        # add the word for the ones place
        if ones > 0 and tens != 1:
            result.append(words[ones])

        # add the scale word
        if i < len(scales):
            result.append(scales[i])

    return ' '.join(result) + '.'