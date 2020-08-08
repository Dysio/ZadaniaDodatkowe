def flatten(aList):
    """
    :param aList:
    :return: Returns a copy of aList, which is a flattened version of aList
    """
    pass
if __name__ == '__main__':
    print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
    assert flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]) == [1, 'a', 'cat', 2, 3, 'dog', 4, 5]