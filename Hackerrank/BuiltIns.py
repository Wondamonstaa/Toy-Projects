#Zip
input_str = input().split()

n = int(input_str[0])
x = int(input_str[1])

[print(sum(i)/len(i)) for i in list(zip(*[list(map(float, input().split())) for _ in range(x)]))]
