

def make_unique_list(lst1):
    return list(set(lst1))

print make_unique_list([1,1,1,1,2,2,2,3,3,3,56])


def mult_all(list2):
    return reduce((lambda x,y: x*y), list2)


print mult_all([3,1,-2,6])
print mult_all([3,1,-2,6])

print [int(x) for x in list('012')]