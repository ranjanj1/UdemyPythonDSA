############ Break #################
from cv2 import bilateralFilter


l = [10,2,4,5,7,9,0]
# x = int(input("enter a number: "))
# for i in l:
#     print(i)
#     if i == x:
#         print("found")
#         break


############# continue ###############

for i in l:
    if i %2 == 0:
        continue
    print(i)