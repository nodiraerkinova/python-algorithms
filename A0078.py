import math

S, P = map(int, input().split())
D = S * S -4 * P
sqrt_D = math.sqrt(D)

if D < 0:
    print(-1)
else:
    if sqrt_D * sqrt_D != D:
        print(-1)
    else:
        x1 = (S - sqrt_D) // 2 
        x2 = (S + sqrt_D) // 2
        print(x1, x2)

