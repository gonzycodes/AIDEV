def ex_1_1():
    card1, card2, card3, card4, card5 = 4, 2, 7, 1, 11
    result = card1 + card2 + card3 + card4 + card5
    return result
    
def ex_1_2():
    card1, card2, card3, card4, card5 = 4, 2, 7, 1, 11
    total = card1 + card2 + card3 + card4 + card5
    return "busted" if total > 21 else "safe"
    raise NotImplementedError("Exercise 1.2 not implemented")

def ex_1_3():
    card1, card2, card3 = 4, 2, 7
    total = card1 + card2 + card3
    if total < 21: 
     return "Safe"
    elif total > 21:
     return "Busted"
    else:
     return "Blackjack"
    raise NotImplementedError("Exercise 1.3 not implemented")

def ex_1_4():
    dealer1, dealer2, dealer3 = 1, 6, 7
    result = dealer1 + dealer2 + dealer3
    if result < 17:
     return "Pick"
    elif 17 <= result < 21:
     return "Stop"
    elif result == 21:
     return "Blackjack"
    else:
     return "Busted"
    
    raise NotImplementedError("Exercise 1.4 not implemented")