# Bank Account Management: Simulate a simple bank account with deposit, withdraw, and balance check functions.

data = {'a':12000,'b':3000, 'c':20000}

def opt1():
    name = input('Enter your full name: ')
    deposit = int(input('Enter the deposit amount: '))
    data[name] = deposit
    print('Your account is successfully created with deposit of ',deposit)

def opt2():
    name = input('Enter account holder name: ')
    deposit = int(input('Enter the deposit amunt: '))
    data [name] = deposit
    print('Successfully deposited!')

def opt3():
    name = input ('Enter your full name: ')
    if data[name]:
        print('Account found.')
    else:
        print('Account not found. Please try again!')
        quit()
    withdrawamt = int(input('Enter the amount you want to withdraw: '))
    if data[name] >= withdrawamt:
        print('Your transaction is successful!')
        data [name] = data[name] - withdrawamt
        a = data[name]
        print('Your balance is now:',a)
    else:
        print('Insufficient Amount in the account.')

def opt4():
    name = input('Enter your acount name: ')
    if data[name]:
        print(name , data[name])
    else:
        print('Account not found!')
        quit()

def main():
    print('******************* BANK MANAGEMENT SYSTEM **********************')

    print('The following choices are available: \n1. To create new account. \n2. To deposit in existing account. \n3. To withdraw from the account. \n4. Check the balance of existing account.')

    n = int(input('Enter your choice...  '))

    if n==1:
        opt1()
    elif n==2:
        opt2()
    elif n==3:
        opt3()
    elif n==4:
        opt4()
    else:
        print('Invalid choice.')

main()
            

