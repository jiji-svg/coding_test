def solution(my_string):
    tmp_set = set()
    new_string = ''
    for i in my_string:
        if i not in tmp_set:
            tmp_set.add(i)
            new_string += i
    answer = new_string
    return answer

