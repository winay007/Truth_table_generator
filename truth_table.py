import itertools


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


def print_table(truth_table, ans, expression=None, variables=None):
    for i in range(len(variables)):
        print(f"   {variables[i]}   |", end=" ")
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
<<<<<<< HEAD

    # separating variables
    # variables = list(set(filter(lambda x: x != None, map(
    #     lambda x: x if x.isalpha() else None, '_'.join(expression).split('_')))))

    # #separating operators
    # operators = list(set(filter(lambda x: x != None, map(
    #     lambda x: x if isValidOperator(x) else None, '_'.join(expression).split('_')))))
    # print(operators)

    # #creating truth  for given number of variables
    # table = list(itertools.product([True, False], repeat=len(variables)))
=======
    # print(check_characters_paranthesis(expression=expression))
    print(valid_expression(expression=expression))

    # variables = list(set(filter(lambda x: x != None,map(lambda x: x if x.isalpha() else None,'_'.join(expression).split('_')))))
    # table = list(itertools.product([True,False], repeat=len(variables)))
>>>>>>> 11d5e96176ceae0b917fb862baba81dab64bce38

    # truth_table = {}

    # for i in range(len(variables)):
    #     var = variables[i]
    #     truth_table[var] = []
    #     for j in range(len(table)):
<<<<<<< HEAD
    #         truth_table[var] = truth_table[var] + [table[j][i]]

    # #final ans
    # ans = implies(truth_table['p'], truth_table['q'])
=======
    #         truth_table[var]  += [table[j][i]]
>>>>>>> 11d5e96176ceae0b917fb862baba81dab64bce38

    # print_table(truth_table=truth_table, ans=ans,variables=variables)
    print(check_valid_chracters(expression=expression))
    # print(check_paranthesis(expression))


def is_validiation(expression):
    if not check_characters_paranthesis(expression):
        return False


<<<<<<< HEAD
def check_paranthesis(expression):
    st = []  # stack for paranthesis chekcing
=======
def check_characters_paranthesis(expression):
    st = [] #stack for paranthesis chekcing
>>>>>>> 11d5e96176ceae0b917fb862baba81dab64bce38

    for i in range(len(expression)):
        char = ord(expression[i])

        # valid characters a-z or A-Z or ( ) or - or < > or ^  or ~ or |
        if not((char >= 65 and char <= 90) or (char >= 97 and char <= 122) or char == 40 or char == 41 or char == 45 or char == 60 or char == 62 or char == 94 or char == 124 or char == 126):
            return False

        # valid paranthesis
        if expression[i] == '(':
            st.append(expression[i])
        else:
            if st and expression[i] == ')':
                if st[len(st)-1] != '(':
                    return False
                else:
                    st.pop()

    return True if not st else False
<<<<<<< HEAD
=======
    
def valid_expression(expression):

    if(not check_characters_paranthesis(expression)):
        return False
    
    operand = []
    operator = []
    i = 0;
    size = len(expression)
    while(i < size):
        print(i)
        print(operand)
        print(operator)
        print(expression[i])
        char = ord(expression[i])
        # ~
        if(char == 126):
            print(char) 
            if operator and operand:
                operator.pop()
                operand.pop()
            
            elif operand:
                return False
            
            operator.append(expression[i])
        # a-z A-Z
        elif((char >=65 and char <=90 ) or (char >=97 and char <=122)):
            if(operand and operator):
                operator.pop() 
                operand.pop()
                operand.append(expression[i])

            elif(not operand and not operator):
                operand.append(expression[i])

            elif(operator[0] == '~'):
                operator.pop()
                operand.append(expression[i])
            
            else : return False
        #  ^ and |
        elif(char == 94 or char == 124):
            if(operand and not operator):
                operator.append(expression[i])
            else : return False

        elif(char == 60):
            if(i +2 < size and expression[i+1] == '-' and expression [i+2] == '>'):
                if(operand and not operator):
                    operator.append("<->")
                    i+=2
                else : return False
            else : return False
        
        elif( char == 45):
            if(i +1 < size and expression [i+1] == '>'):
                if(operand and not operator):
                    operator.append("->")
                    i+=1
                else : return False
            else : return False
        
        elif(char == 41):
            if(operator) : return False
            if(i+1<size):
                char = ord(expression[i+1])
                if((char >=65 and char <=90 ) or (char >=97 and char <=122)):
                    return False

            # operand.pop()        

        i+=1
        print(i)
        print("--")

    if operator:
        return False
    return True

# (p->q)^(q->p)     
>>>>>>> 11d5e96176ceae0b917fb862baba81dab64bce38


def check_valid_chracters(expression):

    for i in range(len(expression)):
        char = ord(expression[i])

        if not((char >= 65 and char <= 90) or (char >= 97 and char <= 122)):
            if(expression[i] == '-' and expression[i+1] != '>'):
                print('1')
                return False
        else:
            if(char != expression[-1]):
                print(char)
                if not(expression[i+1]  == 40 or expression[i+1]  == 41 or expression[i+1]  == 45 or expression[i+1] == 60 or expression[i+1] == 62 or expression[i+1] == 94 or expression[i+1]  == 124 or expression[i+1]  == 126 or expression[i+1]  == 13):
                    print('2')
                    return False

    return True


start()
