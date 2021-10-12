'''
9
3 7 8 5 12 14 21 13 18

9
12
16
'''

def quartile(dataset):

    dataset.sort()

    # decide median is odd or even
    if len(dataset) % 2 : 
        median = dataset[len(dataset) // 2]
    else :
        median = (dataset[len(dataset) // 2] + dataset[(len(dataset) // 2)-1] ) / 2
    # spilt lower and upper list
    median_lower = [i for i in dataset if i < median]
    median_upper = [i for i in dataset if i > median]

    # calulate number of list and decide the way to calculate median lower and higher value
    if len(median_lower) % 2:
        median_lower_val = median_lower[len(median_lower) // 2]
        median_upper_val = median_upper[len(median_upper) // 2]
    else:
        median_lower_val = (median_lower[len(median_lower) // 2] + median_lower[(len(median_lower) // 2)-1] ) / 2
        median_upper_val = (median_upper[len(median_upper) // 2] + median_upper[(len(median_upper) // 2)-1] ) / 2


    print('{:g}'.format(median_lower_val))
    print('{:g}'.format(median))
    print('{:g}'.format(median_upper_val))

input_num = int(input())
num_list = list(int(num) for num in input().strip().split())[:input_num]

quartile(num_list)
