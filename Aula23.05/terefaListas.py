list_num = [30,20,10,40.5,60.5,50,70,80.8,90,100]

list_num.pop(-1)
print(list_num, "\n")

list_num.append(111)
list_num.append(122)
list_num.append(133)
print(list_num, "\n")

list_num.insert(-3, 66)
print(list_num, "\n")

list_num.pop(-3)
print(list_num, "\n")

print("Comprimento:", len(list_num), "\n")

soma = sum(list_num)
print(soma, "\n")

media = (sum(list_num) / len(list_num))
print(media, "\n")

list_num.sort()
print(list_num, "\n")

list_num.sort(reverse=True)
print(list_num, "\n")

list_num.sort()
print(list_num[0], list_num[-1])