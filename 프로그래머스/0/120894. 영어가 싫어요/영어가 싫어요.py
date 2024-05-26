def solution(numbers):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    for i, v in enumerate(nums):
        numbers = numbers.replace(v, str(i))
    return int(numbers)