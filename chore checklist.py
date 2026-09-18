# My Chore Checklist Countdown

# PART 1: Set today's total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!")

# PART 2: Keep a counter for completed chores and the current chore number
completed_count = 0
chore_num = 1

# PART 3: Repeat while there are still chores left to check off
while chore_num <= total_chores:

    # PART 4: Work out the current chore's left to check off
    if chore_num == 1: next_chore = "Tidy your room"
    elif chore_num == 2: next_chore = "Do the laundry"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    # PART 5: Only move on to the next chore once it is marked done
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed.")
    else:
        print("Okay, finish it and check again!")

    # PART 6: Print how many chores remain after each check
    print("Chores remaining:", total_chores - completed_count)
    print()

print("======== ALL CHORES COMPLETE! =========")
print("Great work finishing your entire checklist today!")

print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_count = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_count += 1
    if safety_count == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own)")
        break

print("===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed: ", completed_count)
print("Chores Remaining: ", total_chores - completed_count)
print("=======================")