def expression(inputString):
    exprsnDict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'plus': '+', 'minus': '-', 'multiply': '*', 'divide': '/', 'powerof': '**'}
    mathExprsn, output = "", ""
    while len(inputString) != 0:
        subString = ""
        for letter in inputString:
            subString += letter
            if subString in exprsnDict.keys():
                mathExprsn += exprsnDict.get(subString)
                inputString, subString = inputString.replace(subString, "", 1), ""
                break
    mathExprsn = str(int(eval(mathExprsn)))
    for digit in mathExprsn:
        if digit in exprsnDict.values():
            output += next(key for key, value in exprsnDict.items() if value == digit)
    return output

inputString = input("Enter The Expression:")
print(f"The Output of {inputString} expression is: ", expression(inputString))