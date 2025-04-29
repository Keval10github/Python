last = 0

print("Output:")
for present in range(0, 10):
    sum = last + present
    print(f"Current Number: {present}, Previous Number: {last}, Sum: {sum}")
    last = present
