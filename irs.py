def funct(arg1,arg2,arg3):
    print("arg1",arg1)
    print("arg2",arg2)
    print("arg3",arg3)
    in_val=10


def tfunct(e):

    if e=='0':
        val=0
    if e=='1':
        val-=1
    if e=='2':
        val+=2
    if e=='3':
        val*=3
    if e=='4':
        print(val)
    return val


print(tfunct('0'))
print(tfunct('1'))
print(tfunct('2'))
print(tfunct('3'))
print(tfunct('4'))





#a_set_of_arguments=(1,'2','three')
#funct(*a_set_of_arguments)


#kwargs={"arg3":'three',"arg2":'2',"arg1":1,}
#funct(**kwargs)

#funct(1,'2','three')
#char='abc'
#funct(*char)


