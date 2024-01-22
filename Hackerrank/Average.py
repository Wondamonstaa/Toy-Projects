def average(array):
    # your code goes here
    s = set(array)
    s1 = 0
    for num in s:
        s1 += num
    
    avg = s1/len(s)
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
