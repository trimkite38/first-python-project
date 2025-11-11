print("Welcome to the Football Intro Programme")

player_name = input("Whats your name? ")
position = input ("Whats your position? ")
club = input("Which club do you play for? ")
goals = int(input("How many goals have you scored this season? "))
matches = int(input("How many matches have you played this season?"))
goals_per_match = goals / matches 



print("\n--- Player Profile ---")
print(f"Name: {player_name}")
print(f"Position: {position}")
print(f"Club: {club}")
print(f"Goals this season: {goals}")
print(f"Goals per match: {goals_per_match: .2f}")


# Simple Analysis
if goals >= 20:
    print("You're having an incredible season!")
elif goals >= 10:
    print("Solid achivement , keep pushing!")
else:
    print("Keep training!, More goals are coming!")
if goals_per_match >= 1:
    print("Youre scoring a lot!")
elif goals_per_match >= 0.5:
    print("Good Job, keep improving!")
else:
    print ("Train harder and the goals will come!")
    
print("\nThanks for using the Football Intro Programme!")

# Method 1: Concatenation
print("Player " + player_name + " scored " + str(goals) + " goals,")

# Method 2: f-string 
print(f"{player_name} played {matches} matches and scored {goals} goals.")

# Method 3: Format method 
print("In {} matches, {} scored {} goals. ".format(matches , player_name, goals))

# Ask for matches played
matches = int(input("How many matches have you played this season? "))

# Calculate goals per match 
goals_per_match = goals / matches

print (f"\nGoals per match: {goals_per_match: .2f}")

# Give feedback based on goals per match
if goals_per_match >= 1:
    print("Amazing stats! you're a goal machine!")
elif goals_per_match >= 0.5: 
    print ("Good stats , keep pushing!")
else:
    print("Keep training, more goals are around the corner!")