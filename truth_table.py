import itertools

def implies(p,q):
    ans = []

    for i in range(len(p)):
        if p[i] == True and q[i] == False:
            ans.append( False)
        else:
            ans.append(True)   
    return ans


def negation(p):
    ans = []
    for i in range(len(p)):
            ans.append( not p[i])   
    return ans


def conjuction(p,q):
    ans = []
    for i in range(len(p)):       
        ans.append(p[i] and q[i])
    return ans


def disjuction(p,q):
    ans = []
    for i in range(len(p)):       
        ans.append (p[i] or q[i])
    return ans


def equivalance(p,q):
    ans = []
    for i in range(len(p)):       
        ans.append(p[i] ^ q[i])
    return ans


def print_table(truth_table,ans):
    print("    p   |    q   |    p->q  \n")
    for i in range(len(ans)):
        print(f"{'  True' if truth_table['p'][i] else ' False' }  |{'  True ' if truth_table['q'][i] else '  False'}  |  {ans[i]}\n")


def start():
    expression = input("Enter Propositional logic : ")
    # print(check_characters_paranthesis(expression=expression))
    print(valid_expression(expression=expression))

    # variables = list(set(filter(lambda x: x != None,map(lambda x: x if x.isalpha() else None,'_'.join(expression).split('_')))))
    # table = list(itertools.product([True,False], repeat=len(variables)))

    # truth_table = {}

    # for i in range(len(variables)):
    #     var = variables[i]
    #     truth_table[var] =[]
    #     for j in range(len(table)):
    #         truth_table[var]  += [table[j][i]]

    # ans = implies(truth_table['p'],truth_table['q'])

    # print_table(truth_table=truth_table,ans=ans)
    

def is_validiation(expression):
    if not check_characters_paranthesis(expression):
        return False
    

def check_characters_paranthesis(expression):
    st = [] #stack for paranthesis chekcing

    for i in range(len(expression)):
        char = ord(expression[i])
        
        # valid characters a-z or A-Z or ( ) or - or < > or ^  or ~ or |
        if not((char >=65 and char <=90 ) or (char >=97 and char <=122) or char == 40 or char == 41 or char ==45 or char ==60 or char ==62 or char == 94 or char == 124 or char == 126) : return False

        #valid paranthesis
        if expression[i] == '(' :
            st.append(expression[i])
        else:
            if st and expression[i] == ')' :
                if st[len(st)-1] != '(':
                    return False
                else : st.pop()

    return True if not st else False
    
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


start()