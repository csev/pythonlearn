# Search for lines that contain 'New Revision: ' followed by a number
# Then turn the number into a float and append it to nums
# Finally print the length and the average of nums
import re
fname = input('Enter file:')
hand = open(fname)
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
print(len(nums))
print(int(sum(nums)/len(nums)))
