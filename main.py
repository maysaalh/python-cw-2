# write your code here
# write your code here
my_name= input("what is your name?")
my_age= input("how old are you?")
print(f"my name is {my_name} and i am {my_age} years old ")
#part 2
first_number=13
second_number=67
operation= input("enter the operation")
if operation == "-":
    print(first_number-second_number)
elif operation == "+":
    print(first_number+second_number)
elif operation == "*":
    print(first_number*second_number)
elif operation == "/":
    print(first_number/second_number)
else:
    print(f"the operation is invalid")
#part3
ask_number= input("Enter a number from 1 to 12:")
ask_plural_noun= input("Enter a noun (plural):")
ask_name= input("Enter a name:")
ask_sentence= input("Enter any sentence:")
ask_verb= input("Enter a verb:")
print(f"It was {ask_number} o'clock when I heard a knock at the door.I opened the door and there was a box full of {ask_plural_noun} with a note saying From {ask_name} Just as I closed the door I heard a scream {ask_sentence}. I froze in place and all I could do was {ask_verb}" )
