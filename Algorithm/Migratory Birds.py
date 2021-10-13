from collections import Counter
def migratoryBirds(arr):
    # Write your code here
    c = Counter(arr)
    return c.most_common(1)[0][0]

def migratoryBirds2(arr):
    count = [0]*len(arr)
    
    for i in arr:
        count[i] +=1

    print('max count : ', max(count))
    return count.index(max(count))


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    result2 = migratoryBirds2(arr)
    # print(result, result2, sep=':')
    print(result2)