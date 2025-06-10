total_temp = 0
record_count = 0

while True:
    user_input = input("Enter temperature: ")

    if not user_input.isdigit():
        # skip to the next iteration
        print("Please insert correct number!")
        continue

    temp = int(user_input)
    if record_count != 0:
        if total_temp / record_count > (total_temp + temp) / (record_count + 1):
            print("AVG got colder")
        else:
            print("AVG got hotter")

    total_temp += temp
    record_count += 1
    print(f"AVG: {total_temp / record_count}")
