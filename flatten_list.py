def flatten(aList):
    """
    :param aList:
    :return: Returns a copy of aList, which is a flattened version of aList
    """
    flatten_list = []
    def flatten_nested(aList):
        for elem in aList:
            if type(elem) is list:
                flatten_nested(elem)
            else:
                flatten_list.append(elem)
        return flatten_list
    flatten_nested(aList)

    return flatten_list



if __name__ == '__main__':
    print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
    assert flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]) == [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
