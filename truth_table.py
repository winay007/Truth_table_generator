import itertools
import regex as re
# input = input("Enter proposition")
# input = "p^(q^r^s)"


def implies(p, q):
    ans = []

    for i in range(len(p)):
        # equivalent to implication
        ans.append((not p[i]) or q[i])
    return ans


def negation(p):
    ans = []
    for i in range(len(p)):
        ans.append(not p[i])
    return ans


def conjuction(p, q):
    ans = []

    for i in range(len(p)):
        ans.append(p[i] and q[i])
    return ans


def disjuction(p, q):
    ans = []

    for i in range(len(p)):
        ans.append(p[i] or q[i])
    return ans


def equivalance(p, q):
    ans = []

    for i in range(len(p)):
        ans.append(p[i] ^ q[i])
    return ans


def print_table(truth_table, ans,expression=None,variables=None):
    for i in range(len(variables)):
        print(f"   {variables[i]}   |",end=" ")
    # print("    p   |    q   |    p->q  \n")
    # for i in range(len(ans)):
    #     print(
    #         f"{'  True' if truth_table['p'][i] else ' False' }  |{'  True ' if truth_table['q'][i] else '  False'}  |  {ans[i]}\n")


def isValidOperator(operator):
    if(operator == "->" or operator == "~" or operator == "^" or operator == "∨"):
        return True
    return False


def start():
    expression = input("Enter Propositional logic : ")
 
    #separating variables
    variables = list(set(filter(lambda x: x != None, map(
        lambda x: x if x.isalpha() else None, '_'.join(expression).split('_')))))

    #separating operators
    operators = list(set(filter(lambda x: x != None, map(
        lambda x: x if isValidOperator(x) else None, '_'.join(expression).split('_')))))
    print(operators)

    #creating truth  for given number of variables
    table = list(itertools.product([True, False], repeat=len(variables)))

    truth_table = {}
    
    for i in range(len(variables)):
        var = variables[i]
        truth_table[var] = []
        for j in range(len(table)):
            truth_table[var] = truth_table[var] + [table[j][i]]

    #final ans
    ans = implies(truth_table['p'], truth_table['q'])

    print_table(truth_table=truth_table, ans=ans,variables=variables)


start()
