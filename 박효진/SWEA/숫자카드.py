T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    a_i = list(map(int,input()))
    lst = [0] * 10
    for i in a_i:
        num = lst[i] + 1
        lst[i] = num

    max_count = max(lst)
    max_lst = []
    for i in range(10):
        if lst[i] == max_count:
            max_lst += [i]
    print(f'#{test_case} {max(max_lst)} {max_count}')