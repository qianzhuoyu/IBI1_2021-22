def f(total_money, price):
    remainder = total_money % price  # figure out the rest of the money
    number = (total_money - remainder) / price  # figure out the number of chocolate bars the user can afford
    # return the value
    return 'the user can have ' + str(number) + ' chocolate bars and left ' + str(remainder)


print(f(88, 3))  # example
