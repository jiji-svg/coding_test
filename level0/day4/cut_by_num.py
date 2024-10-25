def solution(my_str, n):
    # pointing = 0
    # answer = []
    # while(pointing < len(my_str)):
    #     if (pointing + n) > (len(my_str) -1):
    #         answer.append(my_str[pointing:])
    #     else:
    #         answer.append(my_str[pointing:pointing+n])
    #     pointing += n
    answer = [my_str[x:x+n] for x in range(0,len(my_str), n)]
        
    return answer

