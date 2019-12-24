number = 1 + 2 * 4 / 6.0
print(number)

remainder = 11 % 3
print(remainder)

msg = "love you bay"
print (msg)

count = 0
while count < 5:
    print(count)
    count += 1 


for i in range(5, 15):
    print(i)

for x in range(3, 8, 2):
    print(x)

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

   