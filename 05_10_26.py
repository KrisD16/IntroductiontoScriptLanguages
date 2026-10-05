n = int(input("Enter a number(> 2): "))

while n < 2:
    n = int(input("Enter a number(> 2): "))


def generate_fibonnaci(n):
    f = [0, 1]
    for _ in range(2, n):
        f.append(f[-1] + f[-2])
    return f


fb = generate_fibonnaci(n)


def total(f):
    return f[0] + f[int(len(f) / 2)] + f[-2]


ttl = total(fb)

print(
    "The fibonnaci list for",
    n,
    "characters:",
    fb,
    "and the sum of the first, the middle and the second to last fibonnaci numbers is:",
    ttl,
    ".",
)
