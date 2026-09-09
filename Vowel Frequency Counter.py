sentence = "learning python is fun"

vowels = "aeiou"

count = 0

for char in sentence:
    if char in vowels:
        count += 1

print(f"the number of vowels are:{count}")