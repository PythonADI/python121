we_went_to_movies = False
we_ate_popcorn = False
did_we_tell_truth = we_went_to_movies and we_ate_popcorn
print(f"{did_we_tell_truth = }")

# And opreator
print(True and True) # True
print(False and True) # False
print(True and False) # False
print(False and False) # False


# OR Operator
we_went_to_movies = False
we_went_to_park = False
did_we_tell_truth = we_went_to_movies or we_went_to_park

print(f"{did_we_tell_truth = }")
print(True or True) # True
print(False or True) # True
print(True or False) # True
print(False or False) # False

# Not Operator
we_went_to_movies = False
we_went_to_park = False
did_we_tell_truth = we_went_to_movies and not we_went_to_park
did_we_lie = not we_went_to_movies or we_went_to_park

print(f"{did_we_tell_truth = }")
print(f"{did_we_lie = }")

A = False
B = False
# print(not(A and B), not A or not B)
