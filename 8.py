x=input("Enter a phrase: ")
n=input("Enter the character you're looking for: ")
if len(n) == 1:
    count = x.count(n)
    print("The character ", n  ,"appears ", count ," times in the phrase.")
else:
    print("Please enter a single character to search for.")