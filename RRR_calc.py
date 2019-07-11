import sys
import pyperclip

def rrr_result(loss):
    print('Stock Name: ' + stock_name)
    print('Amount of Shares: ' + amount_of_shares)
    print('Entry Price: ' + entry_price)
    print('Stop Loss: ' + str(loss))
    #print('Total Price: ' + total_price)

def commission_computation():
    commission = total_amount * 0.0025
    if (commission * 0.0025) > 20:
        return total_amount + commission + (commission * 0.12) + (total_amount * 0.00006) + (total_amount * 0.0001)
    else:
        return total_amount + 22.4 + (total_amount * 0.00006) + (total_amount * 0.0001)

def computation_loop():
    ready_to_paste = 'yes'
    while ready_to_paste == 'yes' or ready_to_paste =='y':
        stop_loss = float(input('Please input a stop loss: '))
        total_price = commission_computation()
        pyperclip.copy(str(rrr_result(stop_loss)))
        # copy_to_clipboard() # TODO: create a function for copy to clipboard.
        print('''Please type y to recompute or n to copy to clipboard.''')
        ready_to_paste = str(raw_input())



if len(sys.argv) > 3:
    stock_name, amount_of_shares, entry_price = sys.argv[1:]
    total_amount = int(amount_of_shares) * float(entry_price)
    computation_loop()
elif sys.argv[1] == '--help':
    print('help instructions') # TODO: improve help instructions
else:
    print('Please type in stock name, share size and price bought.')

