def classify(value):
    if value < 78:
        a = "Below range"
    elif value > 82:
        a = "Above range"
    else:
        a = "In range"
    return a

def calculate_average(total, count):
    return total / count

total = 0
variant1 = 0
variant2 = 0
variant3 = 0
num = int(input("Enter the numbers of ribbons: "))
for _ in range(num):
    num1 = int(input("Enter the ribbon lenght: "))
    res = classify(num1)
    print(res)
    total += num1
    if res == "Below range":
        variant1 += 1
    elif res == "In range":
        variant2 += 1
    elif res == "Above range":
        variant3 += 1

print(f"Total lenght: {total} cm")
print(f"Average lenght: {calculate_average(total, num)} cm")
print(f"Below range: {variant1}")
print(f"In range: {variant2}")
print(f"Above range: {variant3}")