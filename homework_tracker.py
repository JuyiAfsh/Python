total_subjects = 3
original_count = total_subjects
print(f"You have to finsh {original_count} subjects of homework today. Do them on time!")

completed_count = 0
hmr_num = 1

while hmr_num <= total_subjects:

    if hmr_num == 1: next_hmr = "Math"
    elif hmr_num == 2: next_hmr = "English"
    else: next_hmr = "Science"

    answer = input(f"Did you finish {next_hmr}? (yes/no: )")

    if answer == "yes":
        completed_count += 1
        hmr_num += 1
        print("Congrats! Homework complete! Keep going :)")
    else:
        print("Finish your homework and come again!")

    print(f"Homework remaining: {total_subjects - completed_count}")
    print()

print("========== HOMEWORK COMPLETED! ==========")
print("Well done on finishing all you homework :D")

print("===== HOMEWORK CHECKLIST SUMMARY =====")
print("Subjects Assigned Today: ", original_count)
print("Homework Completed: ", completed_count)
print(f"Chores Remaining: {total_subjects - completed_count}")
print("======================================")