#bai 1
list1 = [-1,2,-3,5,7,8,9,-10]
list1 = sorted(list1,key = lambda x : (x if x > 0 else max(list1) - min(list1) + x + 1))
print(*list1) 

#bai 2
list2 = [1,2,3]
list3 = [4,5,6]
list4 = map(lambda x, y : x + y, list2, list3)
print(*list4)

#bai 3
list5 = [19,65,57,39,152,190]
list6 = filter(lambda x : x%13 == 0 or x%19 == 0 , list5)
print(*list6)

#bai 4
list7 = ['php', 'w3r', 'python', 'abcd', 'aaa']
list8 = filter(lambda x : x == x[::-1], list7)
print(*list8)

#bai 5
list9 = [2,4,-6,-9,11,-12,14,-5,17]
duong = sum(filter(lambda x : x > 0, list9))
am = sum(filter(lambda x : x < 0, list9))
print(am, duong)

