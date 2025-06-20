def fn(x):
    # x here is different from global x
    print(x)
    x += 1
    print(x)


x = 29
fn(x)
print(x)
