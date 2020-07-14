# Write a function which will output the range of the calue. 
# Default range is 10%
def range_of_num(num, tolerance_percentage=10):
    tolerance_value = tolerance_percentage *num /100
    return [num - tolerance_value, num + tolerance_value]
print(range_of_num(num=40))
print(range_of_num(num=40, tolerance_percentage=20))