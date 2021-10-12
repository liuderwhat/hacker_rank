'''
1. insert i e : Insert integer at position .
2. print : Print the list.
3. remove e : Delete the first occurrence of integer .
4. append e : Insert integer at the end of the list.
5. sort : Sort the list.
6. pop : Pop the last element from the list.
7. reverse : Reverse the list.
'''

def insert(my_list, index, value):
    my_list.insert(index, value)

def remove_ele(my_list, value):
    my_list.remove(value)

def append_ele(my_list, value):
    my_list.append(value)

def sort_list(my_list):
    my_list.sort()

def pop_ele(my_list):
    my_list.pop()

def reverse(my_list):
    my_list.reverse()

my_list = []
tmp_list = []
show_list = []
num_com = int(input())

while(num_com):
    num_list = list(num for num in input().strip().split())
    
    if num_list[0] == 'insert':
        insert(my_list, int(num_list[1]), int(num_list[2]))
    elif num_list[0] == 'print':
        tmp_list = my_list * 1
        show_list.append(tmp_list)
    elif num_list[0] == 'remove':
        remove_ele(my_list, int(num_list[1]))
    elif num_list[0] == 'append':
        append_ele(my_list, int(num_list[1]))
    elif num_list[0] == 'sort':
        sort_list(my_list)
    elif num_list[0] == 'pop':
        pop_ele(my_list)
    elif num_list[0] == 'reverse':
        reverse(my_list)

    num_com = num_com - 1

for i in show_list:
    print(i)
