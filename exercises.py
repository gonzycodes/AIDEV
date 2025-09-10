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

def ex_2_1():
    my_fruit = "plum"

    match my_fruit:
      case "banana":
        return("The banana is yellow")
      case "apple":
        return("The apple is green")
      case "kiwi":
        return("The kiwi is green")
      case "plum":
        return("The plum is purple")  
    
    raise NotImplementedError("Exercise 2.1 not implemented")


def ex_2_2():
    my_fruit = "pear"

    match my_fruit:
      case "banana":
        return("The banana is yellow")
      case "apple":
        return("The apple is green")
      case "kiwi":
        return("The kiwi is green")
      case "plum":
        return("The plum is purple")
      case _:
        return("That is an unknown fruit")  
   
    raise NotImplementedError("Exercise 2.2 not implemented")

def ex_3_1():
    """
    Exercise 3.1 (1p)
    Use a for-loop to increase 481 by 6 ten times.
    Return the result.
    """
    # TODO: Write your code here
    number = 481
    for _ in range (10):
      number += 6
      return number
    raise NotImplementedError("Exercise 3.1 not implemented")

def ex_3_2():
    """
    Exercise 3.2 (1p)
    Use a for-loop to decrease 551 by 8 ten times.
    Return the result.
    """
    # TODO: Write your code here
    number = 551
    for _ in range (10):
      number -= 6
      return number
    raise NotImplementedError("Exercise 3.2 not implemented")
