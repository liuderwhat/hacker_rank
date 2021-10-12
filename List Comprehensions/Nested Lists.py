if __name__ == '__main__':
    stu_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu_list.append([name, score])
    
    # 先依照分數排序
    stu_list_value = sorted(stu_list, key = lambda s: s[1])
    
    # 找出第二小的所有名字
    min_score = stu_list_value[0][1]
    second_stu_name = []
    sec_score = min_score
    for i in stu_list_value:
        if min_score < i[1]:
            
            if second_stu_name:
                if i[1] == sec_score:
                    second_stu_name.append(i[0])
            else :
                sec_score = i[1]
                second_stu_name.append(i[0])

    # 對名字做排序
    second_stu_name.sort()

    for i in second_stu_name:
        print(i)