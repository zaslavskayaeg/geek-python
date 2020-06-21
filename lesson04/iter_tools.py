from itertools import count

# def sime_number(start=0)
#     yield start + 1

for x in count(100, 10):
    if x > 200:
        break

    print(x)

# a = 0
# while True:
#     a += 2
#     pass

print("Done")
