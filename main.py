import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3


# this is an dictionary 
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values = {
    "A": 2,
    "B": 6,
    "C": 3,
    "D": 2
}


def check_winings(columns , lines , bet , values):
    winnings = 0
    winning_lines = []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings , winning_lines



def get_slot_machine_spin(ROWS , COLS , symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)


    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end = " | " )
            else:
                print(column[row] , end=" ")

        print()

def deposit():
    while True:
        amount = input("What would u like to deposit ? $$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amout must be greater then zero . ")
        else:
            print("please enter a number .")

    return amount
    
    
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <=MAX_LINES:
                break
            else:
                print("Enter Valit number of lines.")
        else:
            print("please enter a number .")

    return lines



def get_bet():
    while True:
        amount = input("What would u like to bet on each line ? $$ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amout must be ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number .")

    return amount

    

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        remaining_balance = balance - total_bet

        if total_bet > balance:
            print(f"You do not have enough to bet that amount , your current balanece is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    print(f"Your remaining balance is ${remaining_balance}")
    slots = get_slot_machine_spin(ROWS , COLS , symbol_count)
    print_slot_machine(slots)
    winnings , winnings_lines= check_winings(slots , lines , bet , symbol_values)
    print(f"you won ${winnings}.")
    print(f"You won on lines: ",*winnings_lines)
    return winnings- total_bet 
 
def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to play (q to quit) .")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left wuth ${balance} ")
main()



