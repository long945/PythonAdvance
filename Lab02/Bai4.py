ids =  [4353, 2314, 2956, 3382, 9362, 3900]
print('Tất cả phần tử trong list là :',ids)
#cau a
ids.remove(3382)
print('Phần tử đã được xóa là :',ids)
#cau b
s = ids.index(9362)
print('Vị trí cần tìm là:',s)
#cau c
a = 4499
ids.insert(ids.index(9362+1),a)
print('Thêm 4499 sau 9362:',ids)
#cau d
b = [5566,1830]
ids.extend(b)
print('Thêm vào : ',ids)
#cau e 
ids.reverse()
print('Dao nguoc:' , ids)
#cau f
ids.sort()
print('Thứ tự từ bé đến lớn:' , ids)
