#iterable = (1,2,3,4,5)
#for i in iterable:
#    print(i)
#----------------------------------
# writes hi for each character in "iterable"
#for i in "iterable":
#    print("hi")
#----------------------------------
# when you dont wanna use the name of the variable inside the loop:
#for _ in "welcome":
#    print("hi")
#----------------------------------
#for i in str(100):     #for i in "100"
#    print(type(int(i)), ":", int(i))
#----------------------------------
# from 1 to 10 (we write 11 cuz it stops before 10)
#for i in range(1, 11,1):
#    print(i)
#----------------------------------
          #محور i,j
#i= 1, 2, 3
#j= 10, 20, 30, 40, 50, 60
for i in range(1,4):
    for j in range(10, 61, 10):
        print(i, ":", j)
#first holds the same i for all js and print them then goes for the outside for and goes to the next i and so on.
#----------------------------------



