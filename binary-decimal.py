print("Binary converter 1.0")
#convert decimal to binary
def decimal_convert(decimal):
    decimal=int(decimal)
    binary_result = ""# result binary number from decimal
    while decimal > 0:
        binary_result = str(decimal % 2) + binary_result
        decimal =int(decimal / 2)
    print(binary_result, "2")

#convert binary to decimal
def binary_convert(binary):
    binary=str(binary)
    decimal_result = 0 # result decimal from binary number
    for i in binary:
        decimal_result = decimal_result*2 +int(i)
    print (decimal_result, "10")

number, swich = map(int, input().split())
if swich == 2:
    binary_convert(number)
elif swich == 10:
    decimal_convert(number)

#no save
