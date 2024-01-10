# https://app.codesignal.com/challenge/pRuhLib5DdetsY4E7
def solution(prices, notes, x):
    def reverse_percentage(current_price, percentage_change):
        # Calculate the original price based on the percentage change
        percentage_from_original_price = 100 + percentage_change
        one_percent = current_price / percentage_from_original_price
        return one_percent * 100

    def parse_percentage_from_note(note):
        # Extract the percentage change from the note
        tokens = note.split(' ')
        if tokens[0] == 'Same':
            return 0
        multiplier = 1 if tokens[1] == 'higher' else -1
        return multiplier * float(tokens[0].rstrip('%'))

    # Calculate the total overpayment
    total_difference = sum(
        current_price - reverse_percentage(current_price, parse_percentage_from_note(note))
        for current_price, note in zip(prices, notes)
    )

    # Compare the total overpayment with the price sensitivity
    return round(total_difference, 5) <= x
