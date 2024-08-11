# Temperature Converter: Write a program that converts temperatures between Celsius and Fahrenheit.

cof = input ('Do you want to convert celsius to Fahrenheit (Y/N)?')

if cof != 'Y' or 'y' or 'N' or 'n' :
    print('Given value is not Y nor N.')
    quit()

if cof == 'Y' or 'y' :
    try:
        cc = int(input('Enter tempreture in Celcius.(Only the number)'))
    except:
        print ('Given Value is Incorrect')
        quit()
    f = (cc * 9 / 5) + 32
    print('The tempreture in fahrenheit is: ', f)
elif cof == 'N' or 'n' :
    try:
        ff = int(input('Enter tempreture in Fahrenheit.(Only the number)'))
    except:
        print ('Given Value is Incorrect')
        quit()
    c = (ff - 32) * 5 / 9
    print('The tempreture in celcius is: ', c)
