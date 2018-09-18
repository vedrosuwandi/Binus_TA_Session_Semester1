Time = int(input("Time Spent :"))
Accel = int(input("Acceleration :"))
Dist = int(input("Total Distance :"))
velocity = Accel * Time
distance = (1/2)*Accel*Time*Time


for x in range (0 , Time + 1) :
    ds =  1/2 * Accel * x * x
    i = int(ds/10)
    print("Duration: ",x,"Dist :", "*" * i)

if velocity > 60 :
    print("The person went over the speed limit", "The max speed",velocity)
else :
    print("The person did not go over the speed limit", "the max speed",velocity)

if distance >= Dist:
    print("The person reached the destination",Dist)
else :
    print("The person did not reach the destination",Dist)