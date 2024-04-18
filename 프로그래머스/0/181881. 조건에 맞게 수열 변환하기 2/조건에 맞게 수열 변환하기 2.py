def solution(arr):
    idx = 0
    prev = arr
    while True:
        new_arr = []
        for i in prev:
            if i >= 50 and i % 2 == 0: new_arr.append(int(i / 2))
            elif i < 50 and i % 2 == 1: new_arr.append(i * 2 + 1)
            else: new_arr.append(i)

        same = all(a == b for a, b in zip(prev, new_arr))
        if same:
            break
        idx += 1

        prev = new_arr
    
    return idx

#같음을 비교하는 과정에서 조금 걸렸는데 결국 정답을 보게 되었다. all과 zip을 왜 생각 못했는지 너무 아쉽다