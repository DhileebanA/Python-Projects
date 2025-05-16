def find(t,l):
    result=0
    for x in l:
        result+=t.count(x)
    return result
    
tup_num = ('a', 'a', 'c', 'b', 'd')
list_num = ['a', 'b','c']

print(find(tup_num,list_num))
