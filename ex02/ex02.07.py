print("Nhap cac dong van ban(Nhap 'done' de ke thuc): ")
lines =[]
while True:
    Line = input()
    if Line.lower() == 'done':
        break
    lines.append(Line)

print("\n cac dong da nhap sau khi chuyen thanh chu in hoa: ")
for line in lines :
    print(line.upper())