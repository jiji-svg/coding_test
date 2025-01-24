def solution(nums):
    
    # 최대값 이하의 소수들 구하기
    def is_prime(num):
        all_set = set(i for i in range(2, num+1))
        for x in range(2, num+1):
            if x in all_set:
                all_set -= set(range(2*x, num+1, x))
        return all_set
    
    # parameters
    nums = list(set(nums))
    new_nums = []
    length = len(nums)-2
    answer = 0
    
    # 3개 합 전부 구하기

