"""
search_in = [2, 3, 4, 5]
element = 4

თითოეული რიცხვისთვის და ინდექსისთვის (x, i) რომელიც არის search_in ლისტში გავაკეთოთ შემდეგი:
    თუ x არის e -ს ტოლი:
        დავაბრუნოთ i
    თუ არადა:
        გავაგრძელოთ შემდეგი იტერაცია

დავაბრუნოთ -1

"""

def find_element(element, search_in):
    # parameter nums shadows global nums variable
    for i, x in enumerate(search_in):
        if x == element:
            return i

    return -1


print(find_element(5, [7, 8, 9, 10, 5]))
print(find_element(5, [7, 8, 9, 10]))
print(find_element(7, [7, 8, 9, 10]))
print(find_element("Nick", ["Luka", "Nick", "George"]))
