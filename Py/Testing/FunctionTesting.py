# Function Test

print map(lambda x: len(x), 'How long are the words in this phrase'.split(' '))

print reduce(lambda x,y: x * 10 + y, [3,4,3,2,1])

print filter(lambda x: x[0] == 'h', ['hello','are','cat','dog','ham','hi','go','to','heart'])

# print zip(['A','B'],['a','b'],'-')
# print zip(['A','B'],['a','b'])

def concatenate(L1, L2, connector):
    # con = list(connector) * 2
    # zipLs = zip (L1, con, L2)
    # return [''.join(x) for x in zipLs]
    return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]
print concatenate(['A','B'],['a','b'],'-')


def d_list(L):
    # blank_dict = {}
    # for val, key  in enumerate(L):
    #     blank_dict[key]=val
    # return blank_dict
    return {key:value for value,key in enumerate(L)}
print d_list(['a','b','c'])

def count_match_index(L):
    # count = 0
    # for val, key in enumerate(L):
    #     if val == key:
    #         count += 1
    # return count
    return len([num for count,num in enumerate(L) if num == count])
print count_match_index([0,2,2,1,5,5,6,10])