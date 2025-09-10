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

    number = 481
    for _ in range (10):
      number += 6
      return number
    raise NotImplementedError("Exercise 3.1 not implemented")

def ex_3_2():
    
    number = 551
    for _ in range (10):
      number -= 6
      return number
   
    raise NotImplementedError("Exercise 3.2 not implemented")


def ex_3_3():
    """
    Exercise 3.3 (3p)
    Use a for-loop to build a string with all even numbers in the range
    22..45, separated by commas. No extra comma at the end.
    """
    # TODO: Write your code here
    number = []
    for i in range(22, 46):
       if i % 2 == 0:
        number.append(str(i))
    return ",".join(number)
    
    raise NotImplementedError("Exercise 3.3 not implemented")

def ex_4_1():
    """
    Exercise 4.1 (1p)
    Use a while-loop to increase 10 by 6 until the value is at least 481.
    Return the number of steps.
    """
    # TODO: Write your code here
    value = 10
    steps = 0
    while value < 481:
      value = value + 6
      steps = steps +1
    return steps
    raise NotImplementedError("Exercise 4.1 not implemented")

def ex_4_2():
    """
    Exercise 4.2 (1p)
    Use a while-loop to subtract 8 from 551 until the value is <= 0.
    Return the number of steps.
    """
    # TODO: Write your code here
    value = 551
    steps = 0
    while value > 551:
      value = value - 8
      steps = steps + 1
    return steps
    raise NotImplementedError("Exercise 4.2 not implemented")


def ex_4_3():
    """
    Exercise 4.3 (3p)
    Use a while-loop to create a comma-separated string of all numbers
    between 28..63 that are divisible by 5 or 7.
    """
    # TODO: Write your code here
    number = 28
    result_list = []
    while number <= 63:
     if number % 5 == 0 or number % 7 == 0:
        result_list.append(str(number))
     number += 1

    result = ",".join(result_list)
    return result

    raise NotImplementedError("Exercise 4.3 not implemented")

def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")
    _run_and_print(ex_3_1, "3.1")
    _run_and_print(ex_3_2, "3.2")
    _run_and_print(ex_3_3, "3.3")
    _run_and_print(ex_4_1, "4.1")
    _run_and_print(ex_4_2, "4.2")
    _run_and_print(ex_4_3, "4.3")


if __name__ == "__main__":
    main()