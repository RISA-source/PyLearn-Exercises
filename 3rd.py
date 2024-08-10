# Temperature Converter: Write a program that converts temperatures between Celsius and Fahrenheit.

cof = input ('Do you want to convert celsius to Fahrenheit (Y/N)?')
if cof == 'Y' or 'y' :
    try:
        cc = int(input('Enter tempreture in Celcius.(Only the number)'))
    except:
        print ('Given Value is Incorrect')
        quit()
