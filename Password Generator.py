import random
import string
password=[]
def ask_pass():
    print("Welcome to the Password Generator!")
    input_pass=int(input("Enter the total numver of characters in the password:"))
    ask1=int(input(f"Enter the number of letters in the password:({input_pass}) "))
    ask2=int(input(f"Enter the number of numbers in the password:({input_pass-ask1})"))
    n=ask1+ask2
    ask3=int(input(f"Enter the number of symbols in the password:({input_pass-n})"))
    totale_ask=ask1+ask2+ask3
    if totale_ask>input_pass:
        print("Invalid input. The sum of seters, numbers, and symbols doesm't match the password")
    else:
        password1=random.choices(string.ascii_letters, k=ask1)+random.choices(string.digits, k=ask2)+random.choices(string.punctuation, k=ask3)
        password=password1
        random.shuffle(password)
        print("".join(password))
ask_pass()
ask_agin=input("Do you want try agin :(yes,no)")
while ask_agin.lower()=="yes":
    ask_pass()
    ask_agin=input("Do you want try agin :(yes,no)")    
print("thank you ")
    