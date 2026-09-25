'''
1. Student Attendance Analysis
Longest continuous sequence without duplicate IDs
'''
#PROGRAM
'''
a = list(map(int, input().split()))
result = set()
left = 0
maximum = 0
for right in range(len(a)):
    while a[right] in result:
        result.remove(a[left])
        left += 1

    result.add(a[right])
    maximum = max(maximum, right - left + 1)

print("Maximum value of length",maximum)
'''
'''
2. Online Shopping Price Analysis
'''
#PROGRAM

a = list(map(int, input().split()))

current = a[0]
maximum = a[0]

for i in range(1, len(a)):
    current = max(a[i], current + a[i])
    maximum = max(maximum, current)

print(maximum)