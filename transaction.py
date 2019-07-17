customer = ['fullname', 'type of account',500]
balance= customer.pop(2)
def deposit(balance,Amnt_deposit):
    balance = balance + Amnt_deposit
    return balance

def withdrawal(balance,Wid_Amnt):
    balance = balance -Wid_Amnt
    return balance
print('your balance after deposit is',deposit( balance,500))
print('your balance after withdrawal is',withdrawal(balance,300))


#print(balance)
