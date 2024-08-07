def solution(number, k):
    n = len(number)
    stack = []
    for num in number:
        while k > 0 and stack and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack)[: n - k]