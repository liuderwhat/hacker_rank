'''
6
6 12 8 10 20 16
5 4 3 2 1 5

9.0
'''


def quartile(dataset):

    # decide median is odd or even
    median_index = len(dataset) // 2

    # spilt lower and upper list
    if len(dataset) % 2:
        median_lower = dataset[:median_index]
        median_upper =  dataset[median_index:]
    else:
        median_lower = dataset[:median_index]
        median_upper =  dataset[median_index+1:]

    # calulate number of list and decide the way to calculate median lower and higher value
    if len(median_lower) % 2:
        median_lower_val = median_lower[len(median_lower) // 2]
        median_upper_val = median_upper[len(median_upper) // 2]
    else:
        median_lower_val = (median_lower[len(median_lower) // 2] + median_lower[(len(median_lower) // 2)-1] ) / 2
        median_upper_val = (median_upper[len(median_upper) // 2] + median_upper[(len(median_upper) // 2)-1] ) / 2
    
    # return median_upper_val - median_lower_val

    # print('{:g}'.format(median_lower_val))
    # print('{:g}'.format(median))
    # print('{:g}'.format(median_upper_val))
    print('{:.1f}'.format(median_upper_val - median_lower_val))


def cal_interquartile(input_num, dataset, freq):
    
    com_dataset = []
    for i, v in enumerate(dataset):

        freq_number = freq[i]

        for x in range(freq_number):
            com_dataset.append(v)

    # com_dataset = [i for i in dataset for x in range(freq[len(freq)%input_num]) ]
    com_dataset.sort()
    
    quartile(com_dataset)

    


input_num = int(input())
num_list = list(int(num) for num in input().strip().split())[:input_num]
freq_list = list(int(num) for num in input().strip().split())[:input_num]
cal_interquartile(input_num, num_list, freq_list)