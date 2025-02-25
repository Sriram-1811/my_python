num=int(input('enter a number:'))

def sum_of_digits(number):
    number = abs(number)
      
    sum = 0
    
    for char in str(number):
        sum += int(char)
    
    return print(sum)

sum_of_digits(num)