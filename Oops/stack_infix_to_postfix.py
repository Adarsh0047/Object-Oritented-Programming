operators=set(['+','-','*','/','(',')','^'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}

def infixtopostfix(expression):
    stack=[]
    output=""
    for ch in expression:
        if ch not in operators:
            output=output+ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output=output+stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[ch]<=priority[stack[-1]]:
                ouput=output+stack.pop()
            stack.append(ch)
    while stack:
        output=output+stack.pop()
    return output

expression = input('Enter infix expression: ')

print('Infix expression: ',expression)

print('Postfix expression: ',infixtopostfix(expression))
    
