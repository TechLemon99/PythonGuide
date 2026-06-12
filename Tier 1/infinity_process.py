num = 180
num_reverse = int("".join(reversed(str(num))))

num2 = (num + num_reverse)
sorted_num2 = int("".join(sorted(str(num2))))
num_reverse2 = int("".join(reversed(str(sorted_num2))))

num3 = (sorted_num2 + num_reverse2)
sorted_num3 = int("".join(sorted(str(num3))))
num_reverse3 = int("".join(reversed(str(sorted_num3))))

num4 = (sorted_num3 + num_reverse3)

print(num)          # 180
print(num_reverse)  # 081

print(num2)         # 261
print(sorted_num2)  # 126
print(num_reverse2) # 621

print(num3)         # 747
print(sorted_num3)  # 477
print(num_reverse3) # 774

print(num4)         # 1251