name = input("enter your real name: ")
club = input("enter your club name: ")

member_number = 4
points_earned = 7
event_count = 3
meeting_hours = 0.5
is_active = True

print(f"Name: {name} -> type: {type(name)}")
print(f"Club: {club} -> type: {type(club)}")
print(f"Member Number: {member_number} -> type: {type(member_number)}")
print(f"Points Earned: {points_earned} -> type: {type(points_earned)}")
print(f"Event Count: {event_count} -> type: {type(event_count)}")
print(f"Meeting Hours: {meeting_hours} -> type: {type(meeting_hours)}")
print(f"Is Active: {is_active} -> type: {type(is_active)}")

member_number_text = str(member_number)
points_earned_text = str(points_earned)
event_count_text = str(event_count)
is_active_text = str(is_active)

print(f"Member Number as Text: {member_number_text} -> type: {type(member_number_text)}")
print(f"Event Count as Text: {event_count_text} -> type: {type(event_count_text)}")
print(f"Points as Text: {points_earned_text} -> type: {type(points_earned_text)}")
print(f"Status as Text: {is_active_text} -> type: {type(is_active_text)}")

first_three = name[0:3]
last_letter = [-1:]
badge_code = first_three + last_letter

print(f"First 3 letter of name: {first_three}")
print(f"Last letter of name: {last_letter}")
print(f"Badge Code: {badge_code}")

reversed_club = club[::-1]
print(f"Reversed Club Name: {reversed_club}")

badge_line_1 = "CLUB MEMBER " + badge_code.upper()
