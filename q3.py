def sum_odd(start:int, end:int):
    range_list = []
    for i in range(start, end+1):
        range_list.append(i)
    for n in range_list:
        odd = n % 2
        if odd == 0:
            range_list.remove(n)
    answer = sum(range_list)
    return answer

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"Number range [{start},{end}]")
odd_total = sum_odd(start, end)
print(odd_total)