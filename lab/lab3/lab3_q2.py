from lab3_q1 import twos_powers
from lab3_q1 import reverse_twos_powers

# n = int(input('Enter a positive integer, n: '))
# for i in range(1, n+1):
#     total = sum([num for num in twos_powers(i)])
#     print(total)

#each number is the previous number*2 +1

n = int(input('Enter a positive integer, n: '))
for i in range(1, n+1):
    total = sum([num for num in reverse_twos_powers(i)])
    print(total)

#each value is the previous value + (1/2)** number of values so far
