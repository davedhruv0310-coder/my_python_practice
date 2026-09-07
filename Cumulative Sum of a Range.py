def yo(num1,num2):
    product = num1 * num2
    

    if product <= 1000:
        return product
    else:
        return num1+num2


a = yo(20,30)
print("The result is ",a)

a= yo(40,30)
print("The result is ",a)