input_str=input("Nhap x,Y: ")
demensions = [int(x) for x in input_str.split(',')]
rownum=demensions[0]
colnum=demensions[1]
multilist= [[0 for col in range(colnum)]for row in range(rownum)]
for row in range(rownum):
    for col in range(colnum):
        multilist[row][col]= row*col
        
print(multilist)