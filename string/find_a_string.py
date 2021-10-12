'''
ABCDCDC
CDC

2 總共出現的次數
'''
def count_substring(string, sub_string):
    occur_num = 0
    for i in range(len(string)):

        if i+len(sub_string) <= len(string):
            
            if string[i:i+len(sub_string)] == sub_string:
                occur_num = occur_num  + 1
        else:
            return occur_num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)