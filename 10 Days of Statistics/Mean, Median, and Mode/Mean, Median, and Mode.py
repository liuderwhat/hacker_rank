# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

43900.6
44627.5
4978

Mean, Median, and Mode
'''

def stat(N, mylist):
    
    mean = sum(mylist) / N
    print(mean)

    mylist.sort()
    
    if len(mylist) % 2 == 0:
        median = (mylist[(len(mylist)//2)-1] + mylist[len(mylist)//2]) / 2
    else :
        median = mylist[len(mylist)//2]
    print(median)
    
    freq = {}
    a = 0
    # Creating an empty dictionary
    freq = {}
    for item in mylist:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    
    if max(freq, key=freq.get) == 1:
        mode = min(mylist)
        
    else : 
        mode = max(freq, key=freq.get)

    print(mode)

input_num = int(input())
num_list = list(int(num) for num in input().strip().split())[:input_num]

stat(input_num, num_list)
        
    
