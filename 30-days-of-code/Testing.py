def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

from random import randint

class TestDataEmptyArray(object):

    # returns an empty array
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    data = set()
    for _ in range(5):
        data.add(randint(0, 100))

    # returns an array of size at least 2 with all unique elements
    @staticmethod
    def get_array():
        uni = list(TestDataUniqueValues.data)
        return uni

    # returns the expected minimum value index for this array
    @staticmethod
    def get_expected_result():
        data = TestDataUniqueValues.get_array()
        return data.index(min(data))

class TestDataExactlyTwoDifferentMinimums(object):
    
    data = set()
    for _ in range(5):
        data.add(randint(0, 100))

    new_data = list(data)
    new_data.append(min(new_data))

    # returns an array where the minimum value occurs at exactly 2 indices
    @staticmethod
    def get_array():
        data = TestDataExactlyTwoDifferentMinimums.new_data
        return data

    # returns the expected index
    @staticmethod
    def get_expected_result():
        data = TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))



def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

