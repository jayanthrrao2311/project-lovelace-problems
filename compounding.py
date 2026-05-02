def compound_interest(amount, rate, years):
    new_amount = amount * ((1 + rate) ** years)

    return new_amount