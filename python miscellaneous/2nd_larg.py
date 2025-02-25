"""8. Write a function to find the second largest number in a list."""
def sec_num(lis):
    lis.sort()
    return lis[-2]

list1=[11,22,33,44,55,6,7,8,9]
l2=sec_num(list1)
print(l2)