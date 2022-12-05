from constants import myconstants

bids = {}  # Declaring an empty dictionary to gather information about the bidder and his bidding amount
bidding_completed = False


def find_highest_bidder(bidding_record):
    """ Returns the winner of the auction from a set of bidders """
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is {winner} with a bid of {highest_bid}')


while not bidding_completed:
    name = input('What is your name ? : ')
    price = int(input('What is your bid ? : '))
    bids[name] = price
    should_continue = input('Are there any other bidders? Type "yes or no".\n')
    print(should_continue)
    if should_continue == myconstants.NO:
        bidding_completed = True
        find_highest_bidder(bids)
