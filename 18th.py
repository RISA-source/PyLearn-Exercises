# Email Validator: Validate if a given string is a properly formatted email address.

def main():
    email = input('Enter the E-Mail Address: ')
    special_characters = "!@#$%^&*()_+-=[];:'\",.<>?/|`~"
    if email.count('@') != 1:
        print('Your email is invalid!')
        quit()
    l = email.split('@')
    p1 = l[0]
    p2 = l[1]
    for i in p1:
        if i in special_characters:
            print('The format of the email address is invalid!')
            quit()
    if p2.count('.') != 1:
        print('The email is invalid!')
        quit()
    n,e = p2.split('.')
    if not n or not e:
        print('The email is invalid!')
        quit()
    print('Congratulations, The email is valid.')

main()