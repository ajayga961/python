from collections import deque

text = input("Enter a string: ")

dq = deque()

for ch in text:
    if ch.isalnum():
        dq.append(ch.lower())

palindrome = True

while len(dq) > 1:
    if dq.popleft() != dq.pop():
        palindrome = False
        break

if palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")

