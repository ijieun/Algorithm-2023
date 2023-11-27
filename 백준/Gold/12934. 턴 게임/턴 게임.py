x, y = map(int, input().split())

if x == 0 and y == 0:
    print(0)
else:
    k = 1
    possible = True
    while True:
        # 두 사람이 이긴 횟수의 합이 x와 y의 합과 같아지는 경우
        if x + y == k * (k + 1) // 2:
            break
        # 두 사람이 이긴 횟수의 합이 x와 y의 합보다 크게 되는 경우
        if x + y < k * (k + 1) // 2:
            possible = False
            break
        k += 1

    if not possible:
        print(-1)
    else:
        result = 0
        for i in range(k, 0, -1):
            if x == 0:
                break
            x -= min(x, i)
            result += 1
        print(result)
