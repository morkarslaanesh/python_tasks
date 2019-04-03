def solution(a):

    if len(a) == 1:

        return 1

    suffix_arr = [False] * len(a)
    suffix_arr[len(a) - 1] = True

    for i in range(len(a) - 2, -1, -1):
        suffix_arr[i] = (a[i] <= a[i + 1] and suffix_arr[i + 1])
        answer = 0

    for i in range(0, len(a)):
        if i > 0 and i + 1 < len(a):
            if a[i - 1] <= a[i + 1] and suffix_arr[i + 1]:
                answer += 1

    if a[i] < a[i - 1]:
        break

    elif i == 0:

    if suffix_arr[i + 1]:
        answer += 1

    elif i == len(a) - 1:
        answer += 1

return answer
