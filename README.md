# HCL TRAINING
## First Task:
Collect the test cases from Amazon e-commerce site.

## Excel sheet:
[View the manual testing XL sheet](https://docs.google.com/spreadsheets/d/1ZxDhupjIfR-JdGBGWQFi2L2XLhIpbjBDaOYQ9x-8T80/edit?usp=sharing)

## Second Task
Find the test cases and valid and invalid input from given exercises.

## Excel sheet:
[View the test cases from given exercises XL sheet](https://docs.google.com/spreadsheets/d/1E5XYy5GSTKugYZfok2l5zuTLiBM4PRKT37CBJL46Xq8/edit?usp=sharing)

# Python Programming Exercises
## Programs

### 1. Binary Numbers Divisible by 5

#### QUESTION
Write a Python program that accepts a sequence of comma-separated 4-digit binary numbers and checks which numbers are divisible by 5.


#### Program

```python
s=input().split(",")
result=[]
for i in s:
    if (int(i,2)%5==0):
        result.append(i)
print(",".join(result))
```
### OUTPUT

<img width="890" height="56" alt="image" src="https://github.com/user-attachments/assets/f5d10255-c47a-4fbf-8b5f-6748cbdb31c0" />

### 2. Count Letters and Digits

#### Question
Write a Python program that accepts a sentence and calculates the number of letters and digits.




#### Program

```python
n=input("Enter the sentence:")
letters=0
digits=0
for i in n:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
print("LETTERS: ",letters)
print("DIGITS: ",digits)
```
### OUTPUT

<img width="877" height="92" alt="image" src="https://github.com/user-attachments/assets/b6b70cae-f0e5-47b7-9abb-81d2bf454dc9" />

### 3. Factorial of a Number

#### Question
Write a program which can compute the factorial of a given number. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8


#### Program

```python
n=int(input("Enter the value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
```
## OUTPUT

<img width="817" height="112" alt="image" src="https://github.com/user-attachments/assets/3f5bb022-e6f8-4dcb-ab07-70035fdc5172" />

## Third Task:

Collect the test cases from Spotify music streaming application.

## Excel sheet:
[View spotify testiong sheet](https://docs.google.com/spreadsheets/d/1lbFXAubon78J3puS4FMZVeR0VOGvV2reMxMLGLIGciE/edit?usp=sharing).
