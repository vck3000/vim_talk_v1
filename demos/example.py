# $ python rolling_average.py 2
# 5
# 3
# The rolling average is 4.00
# 2
# The rolling average is 2.50
# 4
# The rolling average is 3.00
# 9
# The rolling average is 6.50
# 1
# The rolling average is 5.00
# 0


import sys

num = int(sys.argv[1])

ls = []

while True:
    user_num = int(input())

    if user_num == 0:
        break

    ls.append(user_num)

    if len(ls) >= num:
        sliced = ls[-num:]
        avg = sum(sliced)/len(sliced)

        print("The rolling average is {:.2f}.".format(avg))
