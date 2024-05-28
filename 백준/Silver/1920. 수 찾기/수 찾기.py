length_1 = int(input())
length_1_ = []

nums = input()
nums = nums.split()

for i in range(length_1) :
    length_1_.append(int(nums[i]))

length_1_ = set(length_1_)

length_2 = int(input())
length_2_ = []

nums = input()
nums = nums.split()

for i in range(length_2) :
    length_2_.append(int(nums[i]))

for i in length_2_ :
    if i in length_1_ :
        print("1")
    else :
        print("0")