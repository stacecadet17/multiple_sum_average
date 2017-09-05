# write code that prints all the odd numbers from 1 to 1000

for count in range(1, 1000):
  if count % 2 == 1:
    print count

# create another program that prints all the multiples of 5 from 5 to 1,000,000
for count in range(5,1000000):
  if(count % 5 == 0):
    print count

# ******************************************************************************

# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
print sum(a)

# ******************************************************************************

# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
