import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

if n >= 2:
    seq=[0]*(n+1)
    seq[1]=1
    seq[2]=2

    for i in range(3,n+1):
        seq[i]=(seq[i-1]+seq[i-2])%15746

    print(str(seq[n]))

else:
    print("1")