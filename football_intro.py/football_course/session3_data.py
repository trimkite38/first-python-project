# --- Writing to a file ---
file  = open("players.txt", "w") # "w" = write mode, creates/overwrites file 

file.write("Joel - 12 goals\n")
file.write("Ozion - 8 goals\n")
file.write("Ibbi - 15 goals\n")
file.write("Tobi - 5 goals\n")
file.write("Joseph - 3 goals\n")


file.close()
print("players saved to players.txt")

file = open("players.txt", "r") # "r" = read mode
content = file.read()
file.close()

print("File contents:")
print(content)

import csv
# --- Writing to CSV --- 
with open("stats.csv", "w", newline= "") as file: 
    writer = csv.writer(file)
    writer.writerow(["Player", "Goals", "Matches"])

    writer.writerow(["Joel", 12, 7])
    writer.writerow(["Ozion", 8,10])
    writer.writerow(["Ibbi", 15,9])
    writer.writerow(["Tobi", 5, 4])
    writer.writerow(["Joseph", 3, 10])

print("CSV file created.")

import csv

players = []

with open("stats.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # skiper header row

    for row in reader:
        player = row[0]
        goals = int(row[1])
        matches = int(row[2])
        gpm = goals / matches
        players.append([player, goals, matches, round(gpm, 2)])

for p in players:
    print(f"{p[0]} scored {p[1]} goals in {p[2]} matches ({p[3]} goals per matches)")
    if gpm >= 1:
        feedback = "Elite finisher"
    elif gpm >= 0.5:
        feedback  = "Strong attacker"
    else:
        feedback = "Nedds Improvement"

print("\n--- Adda New Player ---")

new_player = input("Enter player name: ")
new_goals = int(input("Goals scored: "))
new_matches = int(input("Matches played: "))

with open("stats.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([new_player, new_goals, new_matches])

print (f"{new_player} added to CSV!")