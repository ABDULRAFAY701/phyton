math=int(input("enter your math marks"))
computer=int(input("enter your computer marks"))
english=int(input("enter your english marks"))
chemistry=int(input("enter your chemistry marks"))
pst=int(input("enter your pst marks"))
physic=int(input("enter your physics marks"))
sindhi=int(input("enter your sindhi marks"))
total=((math+computer+english+chemistry+pst+physic+sindhi)*100)/700
if total>=95 and 100:
    print("your percentage is,total","/n","Your Grade is A + +")
elif total>=75 and 80:
    print("your percentage is,total","/n","Your Grade is A+") 
elif total>=62 and 70:
    print("your percentage is,total","/n","Your Grade is B")
elif total>=50 and 61:
    print("your percentage is,total","/n","Your Grade is C")
elif total>= 40 and 49:
    print("your percentage is,total","/n","Your Grade is D")
elif total>=30 and 39:
    print("your percentage is,total","/n","Your Grade is E")
else:
    print("You are Fail")