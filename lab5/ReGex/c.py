#find sequences of lowercase letters joined with a underscore

import re

s = input()
#pattern = r'[a-z]_[a-z]' в этом случае "q_a_z_aq" вывод: q_az_a
pattern2 = r'(?=([a-z]_[a-z]))' 
arr = re.findall(pattern2, s)
if arr:
    print(''.join(arr))
else:
    print("No")

