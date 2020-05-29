while True:
    print("height: ", end="")
    n = int(input())
    if n > 0 and n < 9:
        break

for i in range(n):
    print(' ' * (n-1-i), end="")
    print(('#' * (i+1)) + '  ' + ('#' * (i+1)))



