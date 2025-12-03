players = ["Ibrahim", "Joel", "Ozion"]
goals = [12 , 4 , 15]

print("Players and goals:")
print(players)
print(goals)

print(f"{players[0]} scored {goals[0]} goals")

new_player = input("Enter a new player name : ")
new_goals = int(input(f"How many goals has {new_player} scored? "))

players.append(new_player)
goals.append(new_goals)

print(players)
print(goals)

print("\n-- Player Stats --")
for i in range(len(players)):
    print(f"{players[i]} scored {goals[i]} goals")

for i in range(len(players)):
    gpm = goals [i] / 10 # assume 10 matches for simplicity
    if gpm >= 1:
        print(f"{players[i]}: Goal machine!")
    elif gpm >=0.5:
        print(f"{players[i]}: Good stats keep it up")
    else:
        print(f"{players[i]}: Keep working hard!")

num_players = int(input("How many players to register? "))
players = []
goals = []

for _ in range(num_players):
    name = input("Player name: ")
    scored = int(input("Goals scored: "))
    players.append(name)
    goals.append(scored)

print("\n--- Season Summary ---")
for i in range(len(players)):
    gpm = goals[i] / 10 # Simple assumption: 10 matches
    feedback = "Absolute goal machine!" if gpm >= 1 else "Great stats!" if gpm>= 0.5 else "Keep working!"
    print(f"{players[i]} scored {goals[i]} goals. {feedback}")

# --- Old Mini Project (for reference) ---
# num_players = int(input("How many players  to register? "))
# players = []
# goals = []
# ...
# print("old version here...")

#Football Stats Tracker 
num_players = int(input("How many players to register? "))

players = []
goals = []
matches = []

for _ in range(num_players):
    name = input("Player name: ")
    scored = int(input(f"How many goals did {name} score? "))
    played = int(input(f"How many matches did {name} play?"))

    players.append(name)
    goals.append(scored)
    matches.append(played)

print("\n--- Season Summary ---")

for i in range(len(players)):
    gpm = goals[i] / matches[i] # calculate goals per match
    # feedback based on goals per match 
    if gpm >= 1:
        feedback = "Absolute goal machine!"
    elif gpm >= 0.5:
        feedback = "Great stats!"
    else:
        feedback = "Keep working!"

    print(f"{players[i]} scored {goals[i]} goalsin {matches[i]} matches. ({gpm:.2f} per match) {feedback}")