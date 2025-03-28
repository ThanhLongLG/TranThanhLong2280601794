def truy_cap_phan_tu(tubple_data):
    first_element = tubple_data[0]
    last_element =tubple_data[-1]
    return first_element,last_element

input_tuple =eval(input("Nhap tuple,Vi du (1,2,3): "))
first,last = truy_cap_phan_tu(input_tuple)


print("phan tu dau tien: ",first)
print("Phan tu cuoi cung: ",last)