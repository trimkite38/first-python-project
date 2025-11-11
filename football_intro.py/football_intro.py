print("Welcome to the Football Intro Programme")

player_name = input("Whats your name? ")
position = input ("Whats your position? ")
club = input("Which club do you play for? ")
goals = int(input("How many goals have you scored this season? "))

print("\n--- Player Profile ---")
print(f"Name: {player_name}")
print(f"Position: {position}")
print(f"Club: {club}")
print(f"Goals this season: {goals}")

# Simple Analysis
if goals >= 20:
    print("You're having an incredible season!")
elif goals >= 10:
    print("Solid achivement , keep pushing!")
else:
    print("Keep training!, More goals are coming!")

print("\nThanks for using the Football Intro Programme!")

