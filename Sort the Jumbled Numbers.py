nums = [789,456,123]
mapping = [0,1,2,3,4,5,6,7,8,9]


def sortJumbled(mapping, nums):
     new_nums = []
     for num in nums:
         i= 0
         new_n = 0 
         for k in range(len(str(num))):
             n = num % 10
             new_n += mapping[n] * (10**i)
             num = int(num / 10)
             i += 1
         new_nums.append(new_n)

     new_dict = {}
     for j in range(len(nums)):
         new_dict[nums[j]] = new_nums[j]

     new_dict = dict(sorted(new_dict.items(), key=lambda item: (item[1], item[0])))

     return list(new_dict.keys())

print(sortJumbled(mapping, nums))