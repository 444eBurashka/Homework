nums, n = [], int(input())
while n != 0:
    if len(str(n)) == 2:
        nums.append(n)
    n = int(input())
if nums:
    print(round(sum(nums) / len(nums), 1))
else:
    print('NO')