def feedback(code, guess):
    exact = 0
    remaining_code = []
    remaining_guess = []

    # First, count exact matches
    for code_digit, guess_digit in zip(code, guess):
        if code_digit == guess_digit:
            exact += 1
        else:
            remaining_code.append(code_digit)
            remaining_guess.append(guess_digit)

    # Then, count partial matches from remaining positions
    partial = 0
    for digit in remaining_guess:
        if digit in remaining_code:
            partial += 1
            remaining_code.remove(digit)

    return exact, partial