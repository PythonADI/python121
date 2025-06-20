def fn(a, b, **kwargs):
    print(f'{a = } | {b = } | {kwargs = }')

def f(*args, **kwargs):
    print(f'{args = } | {kwargs = }')

fn(5, 7)
fn(5, b=9)
fn(a=5, b=9)
fn(b=5, a=9, c=7, n=9)

f(6, 7, 8, name="Luka", age=17)
