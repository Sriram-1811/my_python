"""1. Write a Python program to check if a number is even or odd."""

def num(n):
    if n%2==0:
        print("this is an even number")
    else:
        print("this is an odd number")

n=int(input("enter a number:"))
num(n)