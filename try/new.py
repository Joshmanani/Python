# exceptions

#try except finally

try:
    f = open('simple.txt','r')
    f.write('test write')
except:
    print("error couldn't perform action")
#you can use finally instead of else to ignore the except
else:
    print('success!')

print('hello world')
