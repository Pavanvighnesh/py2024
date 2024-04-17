st='print only the words in this sentance that starts with word s'   

print([letter[0] for letter in st.split()])



for words in st.split():
    if words[0]=='s':
        print(words)

mylist=[]
for n in range(3,50,3):
    (mylist.append(n))
print(mylist)

print([x for x in range(1,51) if x%3==0])


print('vighnesh is bad boy')