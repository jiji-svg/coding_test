def solution(n, w, num):
    answer = 0
    boxes = []
    for i in range(1, n+1, w):
        box = []
        for j in range(i,i+w):
            box.append(j)
            
            if j == n:
                for _ in range(len(box),w):
                    box.append(0)
                break
        if boxes==[] or len(boxes)%2==0:
            pass
        else:
            box = box[-1::-1]
        boxes.append(box)
    
    sec_idx = boxes[(num-1)//w].index(num)
    
    for i in range((num-1)//w, len(boxes)):
        n = boxes[i][sec_idx]
        if n != 0:
            answer += 1
    
    return answer
