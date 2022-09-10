from random import choice

print("Enter the number of friends joining (including you):")
number_of_friends = int(input())
print()

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {input().strip(): 0 for _ in range(number_of_friends)}
    print()
    print("Enter the total bill value:")
    final_bill = float(input())
    split_val = round(final_bill / number_of_friends, 2)
    print()
    
    for key in friends:
        friends[key] = split_val

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    response = input()
    print()
    
    if response == "Yes":
        # Choose random name from "friends"
        random_name = choice(list(friends.keys()))
        
        new_split_val = round(final_bill / (number_of_friends - 1), 2)
        
        for key in friends:
            friends[key] = 0 if key == random_name else new_split_val
            
        print(f"{random_name} is the lucky one")
    else:
        print("No one is going to be lucky")
        
    print()
    print(friends)