#s="Malayalam"
s="20BAD066"
print(s)
stack=[]
rev=[]
s_rev=''
for i in range(len(s)):
    stack.append(s[i])
for j in range(len(stack)):
    rev.append(stack[(len(stack)-1)-j])

print(rev)
s_rev=''.join(rev)
print(s_rev)
    
