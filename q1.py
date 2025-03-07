# QUESTION 1

def prc(input_list:list):
    output_list = []
    input_list.sort() #ascending
    for n in range(len(input_list)):
        if input_list[n] % 2 == 0 and input_list[n] != input_list[n-1]:
            output_list.append(input_list[n])
    return output_list

list_a = [1, 4, 5, 2, 9, 8, 8, 6]
print("Input List: ", list_a)
output_list = prc(list_a)
print("Output List: ",output_list)
