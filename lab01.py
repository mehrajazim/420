keywords=['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
f = open('/Users/azimmehraj/Desktop/BRAC /CSE-420/text.txt','r')
lines_List= f.read().splitlines()
lines_Refined=[]
for line in lines_List:
    lines_Refined.append(line.strip())
sureShot_Keywords=[]
identifiers=[]
for line in lines_Refined:
    l=line.split(" ",1)
    word=l[0]
    if word in keywords:
        #if len(l)==2:            
            #
        if word not in sureShot_Keywords:   
            sureShot_Keywords.append(word)

#print(sureShot_Keywords)
