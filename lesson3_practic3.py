# Написать программу, которая выводит саму себя задом наперед
import sys
filename = sys.argv[0]
f = open(filename, 'r')
for line in f:
    print(line[::-1], end='')
n = int(input())
i = 2
while i <= n:
    if(n % i == 0):
      print(i)
    i+=1