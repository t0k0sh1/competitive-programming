A = int(input())
B = int(input())
C = int(input())
X = int(input())

A = min(A, X // 500)
B = min(B, X // 100)
C = min(C, X // 50)

res = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if 500*a + 100*b + 50*c == X:
                res += 1
print(res)