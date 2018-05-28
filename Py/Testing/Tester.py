

# def make_unique_list(lst1):
#     return list(set(lst1))

# print make_unique_list([1,1,1,1,2,2,2,3,3,3,56])


# def mult_all(list2):
#     return reduce((lambda x,y: x*y), list2)


# print mult_all([3,1,-2,6])
# print mult_all([3,1,-2,6])

# print [int(x) for x in list('012')]

# str = "this is how I print things"
# print str
# etc = "this is what it feels like to type on this keyboard"

# print etc
# string = "pylint, y u complain about var names so much."

# def sum(a, b):
#     return reduce(lambda x,y: x+y, [a, b])


# print sum(2, 4)

import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/tmp/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)
