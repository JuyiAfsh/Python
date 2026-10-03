print(" === Classroom Point Calculator === ")
team1 = 36
team2 = 29
team4 = 18
team5 = 37

teams_added = team1 + team2 + team3 + team4 + team5 
average = teams_added / 5

print(f"Total points: {teams_added}")
print(f"Averge per team: {average}")

stars_per_point = 3
total_stars = teams_added * stars_per_point
print(f"Stars earned: {total_stars}")

boxes = total_stars // 25
leftover = total_stars % 25
print(f"Boxes of stars: {boxes}")
print(f"Leftover stars: {leftover}")

last_week = 250
print(f"Better then last week? : {total_stars > last_week}")
print(f"Same as last week? : {total_stars == last_week}")
print()

teams_added += 20
print(f"After bonus points: {teams_added}")

teams_added -= 9
print(f"After missed homework: {teams_added}")

boxes = teams_added * stars_per_point // 25
print(f"Final boxes of stars: {boxes}")