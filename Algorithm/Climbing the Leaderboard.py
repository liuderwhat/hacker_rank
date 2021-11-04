'''
7
100 100 50 40 40 20 10
4
5 25 50 120
'''
def climbingLeaderboard2(ranked, player):
    # 10 20 40 50 100
    # 5  4  3  2  1
    # 讓分數轉set再轉list並作排序
    ranked = list(sorted(set(ranked)))
    # 因為題目有說選手分數會越來越高，所以用cur計數
    cur = 0
    ans = []
    for i in player:

        # 起始直以cur開始(也可以放0)，這邊不管cur便多少，還是會跑len(ranked)-cur
        for x in range(cur, len(ranked)):
            # 當排名不再往前，就計算排名
            # 因為是小到大，所以是用排名數-cur+1
            if ranked[x] > i:
                ans.append(len(ranked)-cur+1)
                break
            # 若可再往前一名，cur就+1，
            else:
                cur = cur + 1
        # 當跑完迴圈就是第一名
        else:
            ans.append(1)

    return ans

def climbingLeaderboard(ranked, player):

    ranked = sorted(ranked)

    # Write your code here
    ans = []
    rank_list = []
    r = 1
    rank_list.append([1,ranked[0]])
    ranked = ranked[1:]
    for i, v in enumerate(ranked):

        if i != len(ranked):

            if ranked[i] != rank_list[len(rank_list)-1][1]:
                r+=1
                rank_list.append([r,v])
            else : 
                rank_list.append([r,v])
    print(rank_list)
    rank_list = sorted(rank_list, reverse = True)
    tmp_score = 0
    cur_rank = rank_list[0][0]

    # for i in player:
    #     flag = False
    #     for x in rank_list:
    #         if tmp_score != x[1]:
    #             if i == x[1]:
    #                 tmp = x[0]
    #             elif i < x[1]:
    #                 ans.append(x[0]+1)
    #                 flag = True
    #                 break
    #             tmp_score = x[1]
    #     if not flag:
    #         ans.append(1)



ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard2(ranked, player)

print(result)