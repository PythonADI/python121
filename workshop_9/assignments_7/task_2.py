"""
გვაქვს:
room რომელიც არის სტრინგების ლისტი
start_pos რომელიც არის რიცხვი და წარმოადგენს ლისტში ჩვენს პოზიციას

შეზღუდვები:
მხოლოდ მიმდინარე პოზიიცდან შემიძლია გადაადგილება. არ შემიძლია თუ ვიმყოფები ინდექს 5-ზე
შევამოწმო ან გადავიდე 0 - ინდექსზე
შემიძლია გადავადგილდე 4-ზე ან 6-ზე და შემიძლია შევამოწმო 5-იანი


ამოხსნა:
pos = start_pos (5)
moving_right = True # right
steps = 0

while True:
    steps += 1
    current_tile = room[pos]
    # searching part
    if current_tile == "😒" (did we find him?):
        end program print step

    # moving part
    if moving_right (we want to move right):
        if room.length <= pos + 1 (next position is a wall):
            moving_right = False # we start moving left
            continue
        
        pos += 1 (let's move right)
        continue
    
    # moving left
    if pos == 0 (next move will be a wall):
        saomething is not right!
    pos -= 1
"""

room = ["", "", "😒", "", "", "", "", "", ""]
starting_position = 0

def find_v1(room, start_pos):
    pos = start_pos
    moving_right = True # right
    steps = 0

    while True:
        steps += 1
        current_tile = room[pos]
        # searching part
        if current_tile == "😒":
            print(f"found him on {pos}")
            return steps

        # moving part
        if moving_right:
            if len(room) <= pos + 1:
                moving_right = False # we start moving left
                continue

            pos += 1
            continue

        # moving left
        if pos == 0:
            print("Misterious man is missing")
            return steps
        pos -= 1

print(find_v1(room, len(room) // 2))
