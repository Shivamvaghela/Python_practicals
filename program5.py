largest_odd = None

print("Enter 10 numbers:")

for i in range(10):
    num = int(input())

    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

if largest_odd is None:
    print("No odd number entered.")
else:
    print("Largest odd number is:", largest_odd)
