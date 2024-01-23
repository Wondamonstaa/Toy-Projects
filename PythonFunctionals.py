#Fibonacci and Lambdas
cube = lambda x: pow(x, 3)

def fibonacci(n):
    
    if n == 1:
        return [0]
    
    x, y, lst = 0, 1, []
    for _ in range(n):
        lst.append(x)
        x, y = y, x + y
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
