def test(nums):
    
    resultlist = []

    for i in range(1,nums):
        if i % 2 == 0:
            resultlist.append(i)
    return resultlist


test(51)