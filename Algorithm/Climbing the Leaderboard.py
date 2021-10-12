'''
7
100 100 50 40 40 20 10
4
5 25 50 120
'''
def climbingLeaderboard2(ranked, player):
    # 10 20 40 50 100
    # 5  4  3  2  1
    ranked = list(sorted(set(ranked)))
    cur = 0
    ans = []
    for i in player:

        for x in range(cur, len(ranked)):

            if ranked[x] > i:
                ans.append(len(ranked)-cur+1)
                break
            else:
                cur = cur + 1

        if cur == len(ranked):
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