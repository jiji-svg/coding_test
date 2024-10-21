def solution(id_pw, db):
    answer = ''
    id1, pw1 = id_pw
    flag = False
    for informations in db:
        id0, pw0 = informations

        if id0 == id1:
            if pw0 == pw1:
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                flag = True
        else:
            if flag == False:
                answer = 'fail'        

    return answer

