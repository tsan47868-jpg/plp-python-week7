items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")

long_name_count = 0
for item in items:
    letter_count = 0
    for character in item:
        if character != " ":
            letter_count += 1
    if letter_count > 4:
        long_name_count += 1

print("Items with more than 4 letters:", long_name_count)

longest_item = items[0]
for item in items[1:]:
    if len(item) > len(longest_item):
        longest_item = item

print("Longest item:", longest_item)