# Hello excercise from Week 0

# Name: Michael Ko


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
#H
pu(bob)
bk(bob, 150)
pd(bob)
lt(bob)
fd(bob, 100)
bk(bob, 50)
rt(bob)
fd(bob, 40)
lt(bob)
fd(bob, 50)
bk(bob, 100)
pu(bob)
rt(bob)
fd(bob, 20)
#E
pd(bob)
lt(bob)
fd(bob, 100)
rt(bob)
fd(bob, 40)
bk(bob, 40)
rt(bob)
fd(bob,50)
lt(bob)
fd(bob, 40)
bk(bob, 40)
rt(bob)
fd(bob, 50)
lt(bob)
fd(bob, 40)
#L
pu(bob)
fd(bob, 20)
pd(bob)
lt(bob)
fd(bob, 100)
bk(bob, 100)
rt(bob)
fd(bob,50)
#L
pu(bob)
fd(bob, 20)
pd(bob)
lt(bob)
fd(bob, 100)
bk(bob, 100)
rt(bob)
fd(bob,50)
#O
pu(bob)
fd(bob, 20)
pd(bob)
for i in range(2):
 fd(bob, 50)
 lt(bob)
 fd(bob, 100)
 lt(bob)

wait_for_user()					
