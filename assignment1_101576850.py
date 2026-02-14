"""
Author: Salem Mohamed Salem Hataish Aljaberi
Assignment: #1
"""

# ==============================
# 1) Variables (with data types)
# ==============================
gym_member = "Alex Alliton"          # str
preferred_weight_kg = 20.5           # float
highest_reps = 25                    # int
membership_active = True             # bool

# ======================================================
# 2) Dictionary: friend name (str) -> minutes tuple (int,int,int)
#    (Yoga, Running, Weightlifting)
# ======================================================
# Dictionary (dict) storing workout minutes as tuples for each friend
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 25),
    "Taylor": (20, 50, 30)
}

# ======================================================
# 3) Add total minutes for each friend into dictionary
# ======================================================
friends = list(workout_stats.keys())

for friend in friends:
    yoga, running, weightlifting = workout_stats[friend]
    total_minutes = yoga + running + weightlifting
    workout_stats[friend + "_Total"] = total_minutes

# ======================================================
# 4) Create 2D (nested) list from workout minutes
# ======================================================
# Nested list (list of lists) where each row is [yoga, running, weightlifting]
workout_list = []
for friend in friends:
    workout_list.append(list(workout_stats[friend]))

# ======================================================
# 5) Slicing requirements
# ======================================================
print("Workout List (2D):", workout_list)
print("\nYoga and Running for all friends (first two columns):")
for row in workout_list:
    print(row[:2])

print("\nWeightlifting for the last two friends (last column, last two rows):")
for row in workout_list[-2:]:
    print(row[2:])

# ======================================================
# 6) If-statement: praise if total >= 120
# ======================================================
print("\nChecking for friends with total minutes >= 120:")
for friend in friends:
    if workout_stats[friend + "_Total"] >= 120:
        print("Great job staying active, " + friend + "!")

# ======================================================
# 7) User input feature: look up a friend
# ======================================================
name = input("\nEnter a friend's name to look up: ").strip()

if name in workout_stats:
    yoga, running, weightlifting = workout_stats[name]
    total = workout_stats[name + "_Total"]
    print("\n" + name + "'s workout minutes:")
    print("  Yoga: " + str(yoga))
    print("  Running: " + str(running))
    print("  Weightlifting: " + str(weightlifting))
    print("  Total: " + str(total))
else:
    print("Friend " + name + " not found in the records.")

# ======================================================
# 8) Highest and lowest total workout minutes
# ======================================================
highest_friend = friends[0]
lowest_friend = friends[0]

for friend in friends:
    if workout_stats[friend + "_Total"] > workout_stats[highest_friend + "_Total"]:
        highest_friend = friend
    if workout_stats[friend + "_Total"] < workout_stats[lowest_friend + "_Total"]:
        lowest_friend = friend

print("\nSummary:")
print("Friend with the highest total workout minutes: " + highest_friend +
      " (" + str(workout_stats[highest_friend + "_Total"]) + ")")
print("Friend with the lowest total workout minutes: " + lowest_friend +
      " (" + str(workout_stats[lowest_friend + "_Total"]) + ")")
