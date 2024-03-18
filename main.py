from re import T


nric = input('Enter an NRIC number: ')
validity = "invalid"
# Type your code below
digit_weight = "2765432"
st_digit = "JZIHGFEDCBA"
fg_digit = "XWUTRQPNMLK"
validity = "invalid"
sum = 0
for i in nric:
    if i.isnumeric() :
        i = int(i)
        if i > 0 and i <8 :
            sum +=i*int(digit_weight[i-1])
checkdigit = sum%11
if nric[0] == "S" or nric[0] == "T":
    checking = nric[8]
    if checking == st_digit[checkdigit]:
        validity = "valid"
if nric[0] == "F" or nric[0] == "G":
    checking = nric[8]
    if checking == fg_digit[checkdigit]:
        validity = "valid"
if nric[0] != "F" and nric[0] != "G" and nric[0] != "S" and nric[0] != "T":
    validity = "invalid"
if len(nric) != 9:
    validity = "invalid"

print(f"The input NRIC is {nric}.")
print(f"NRIC is {validity}.")