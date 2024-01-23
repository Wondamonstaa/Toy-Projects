#Zip
input_str = input().split()

n = int(input_str[0])
x = int(input_str[1])

[print(sum(i)/len(i)) for i in list(zip(*[list(map(float, input().split())) for _ in range(x)]))]


#String composition
s = input()

low, up, odd, even = [], [], [], []

for char in s:
    if char.islower():
        low.append(char)
        low.sort()
    elif char.isupper():
        up.append(char)
        up.sort()
    elif char.isdigit() and int(char) % 2 != 0:
        odd.append(char)
        odd.sort()
    elif char.isdigit() and int(char) % 2 == 0:
        even.append(char)
        even.sort()

result = ''.join(low + up + odd + even)
print(result)
