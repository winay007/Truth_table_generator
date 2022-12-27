import regex as re
# input = input("Enter proposition")
input = "p^(q^r^s)"

varibles = list(filter(lambda x: x != None,map(lambda x: x if x.isalpha() else None,'_'.join(input).split('_'))))





generalize = [
    [True,True,False,False],
    [True,False,True,False],
]

answer = []