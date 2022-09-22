input_string="without,hello,bag,world"

input_list=input_string.split(',')

input_list_sorted=sorted(input_list)


sorted_string=""

for i in input_list_sorted:
    if i!=input_list_sorted[len(input_list_sorted)-1]:
        sorted_string+=i+', '
    else:
        sorted_string+=i

print(sorted_string)





