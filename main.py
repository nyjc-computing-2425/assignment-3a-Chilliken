from re import T


nric = input('Enter an NRIC number: ')
validity = "invalid"
# Type your code below
prefix = nric[0]
numbers = nric[1:8]
suffix = nric[-1]
first_letter = "STFG"
digit_weight = "2765432"
st_digit = "JZIHGFEDCBA"
fg_digit = "XWUTRQPNMLK"
invalidity = "NRIC is invalid."
validity = "NRIC is valid."
print(f"The input NRIC is {nric}.")
if prefix not in first_letter:
    print(invalidity)
elif len(nric) != 9:
    print(invalidity)
elif numbers.isnumeric() is False:
    print(invalidity)
elif numbers.isnumeric():
    sum = (int(numbers[0]) * 2
          + int(numbers[1]) * 7
          + int(numbers[2]) * 6
          + int(numbers[3]) * 5
          + int(numbers[4]) * 4
          + int(numbers[5]) * 3
          + int(numbers[6]) * 2)
    
    if prefix in "TG":
        sum +=4
    
    remainder = sum % 11
    
    checkdigit = ''
    if prefix in "ST":
        checkdigit = st_digit[remainder]
    elif prefix in "FG":
        checkdigit = fg_digit[remainder]
    
    if suffix == checkdigit:
        print(validity)
    else:
        print(invalidity)

    

