[<<Phần 4](../docs-tutorial-py/part4.md) [Phần 6>>](../docs-tutorial-py/part6.md)
# List
Có bốn kiểu thu thập dữ liệu trong Python:
* List: Là một tập hợp được sắp xếp theo thứ tự và có thể thay đổi(Modifiable). Cho phép các thành phần trùng lặp.
* Tuple: Là một tập hợp được sắp xếp theo thứ tự và không thể thay đổi. Cho phép các thành phần trùng lặp.
* Set: Là một tập hợp không có thứ tự, không lập chỉ mục và không thể sửa đổi, nhưng bạn có thể thêm các mục mới. Không có thành phần trùng lặp
* Dictionary:Là một tập hợp không có thứ tự, có thể thay đổi và được lập chỉ mục. Không có thành phần trùng lặp.

List là tập hợp các kiểu dữ liệu khác nhau được sắp xếp theo thứ tự và có thể sửa đổi(Có thể thay đổi). Một danh sách có thể trống hoặc nó có thể các mục hoặc các kiểu mục dữ liệu khác nhau.

## Tạo list
Trong python, chúng ta có thể tạo danh sách theo hai cách

```
LIST = list()

empty_list = list()
print(len(empty_list))
```
Sử dụng dấu ngoặc vuông
```
LIST=[]
empty_list = []

lst = ['Duong', 'Huy', 'ESVN'] 
print(lst) # ['Duong', 'Huy', 'ESVN'] # in biến lst
print('Số lượng bien:', len(lst)) #3 #In ra số lượng biến
```

Danh sách có thể có các kiểu mục thuộc các kiểu dữ liệu khác nhau:
```
lst = ['Duonghuy', 16, True, {'country':'Vietnam', 'city':'Hanoi'}]
print(lst)
print(len(lst))
---

['Duonghuy', 16, True, {'country': 'Vietnam', 'city': 'Hanoi'}]
4
```

### Truy cấp các item trong list bằng các sử dụng Indexing
```
Qua = ['chuoi', 'oi', 'tao', 'xoai', 'ot']
Qua1 = Qua[0]
print(Qua1)     #Chuoi

Qua2= Qua[2]
print(Qua2)     #tao

Quacuoi = len(Qua) -1
quacuoi = Qua[Quacuoi]
print(quacuoi)          #ot
```

### Truy cập các mục trong danh sách bằng cách sử dụng item Negative indexing 
Negative indexing có nghĩa là bắt đầu từ cuối, -1 là item cuối cùng, -2 là item cuối cùng thứ 2.

### Unpacking List Items
```
lst = ['item','item2','item3', 'item4', 'item5', 'item nnn']
item_dautien, item_thu2, item_thu3, *rest = lst
print(item_dautien)     # item1
print(item_thu2)    # item2
print(item_thu3)     # item3
print(rest)         # In ra các item còn lại
```

## In ra các số
```first, second, third,*rest, nine, tenth = [1,2,3,4,5,6,7,8,9,10]

print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8]
print(nine)           # 9  
print(tenth)          # 10  
```
## In ra chuỗi list
```
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) # Germany
print(fr) #France
print(bg) #Belgium
print(sw) #Sweden
print(scandic) #['Denmark', 'Finland', 'Norway', 'Iceland']
print(es) #Estonia
```

## Positive Indexing
Chỉ dịnh một loạt các positive indexes bằng chỉ định bắt đầu, kết thúc và bước nhảy, giá trị trả về sẽ là một danh mới.
```
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:2] #['banana', 'orange'] In ra kết quả bắt đầu từ 0 kết thúc 2
all_fruits = fruits[0:] # In ra tất cả
orange_and_mango = fruits[1:3] #['orange', 'mango']
orange_mango_lemon = fruits[1:] #['orange', 'mango', 'lemon']
orange_and_lemon = fruits[::2] #['banana', 'mango'] 

nums = ['1', '2', '4', '5', '6', '9', '10']
num = nums[::3] #['1', '5', '10']
num = nums[::4] #['1', '6']
num = nums[-4:] #['5', '6', '9', '10'] 4 item cuối cùng
num = nums[-2:] #['9', '10'] 2 item cuối cùng
num = nums[-3:-1] #['6', '9']
num = nums[-3:] #['6', '9', '10']
num = nums[::-1] #['10', '9', '6', '5', '4', '2', '1']
```

### Sửa đổi list
Danh sách là một tập hợp các mục có thứ tự có thể thay đổi hoặc sửa đổi được. Cho phép sửa đổi list.
```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado' #['avocado', 'orange', 'mango', 'lemon'] 

nums = ['1', '2', '33', '4', '-5', '-6', '10']
nums[2] = '3' #['1', '2', '3', '4', '-5', '-6', '10']
nums[4] ='5' #['1', '2', '3', '4', '5', '-6', '10']
lastnum= len(nums) -1
nums[lastnum] ='7' #['1', '2', '3', '4', '5', '-6', '7']
```
## Kiểm tra các items trong danh sách
```
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) # True có banana trong list

does_exist = 'lime' in fruits
print(does_exist) # False Không có lime trong list
```

## Thêm các Item vào List
```
# syntax
lst = list()
lst.append(item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple') # ['banana', 'orange', 'mango', 'lemon', 'apple']
print(fruits)
fruits.append('lime')#['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```
## Chèn các mục vào danh sách
Sử dụng phương thức insert() để thêm 1 item vào list. Lưu ý các mục được chèn vào bên phải
```
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'Bưởi') 
print(fruits) #['banana', 'orange', 'Bưởi', 'mango', 'lemon']

fruits.insert(4, 'Mít')
print(fruits) # ['banana', 'orange', 'Bưởi', 'mango', 'Mít', 'lemon']
```

## Xóa các iterm khỏi danh sách
```
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

```
fruits= ['banana', 'orange', 'Bưởi', 'mango', 'Mít', 'lemon']
fruits.remove('banana')
print(fruits) #['orange', 'Bưởi', 'mango', 'Mít', 'lemon']
fruits.remove('orange') 
print(fruits) #['Bưởi', 'mango', 'Mít', 'lemon']
```
### Xóa Item bằng cách sử dụng pop
```
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

```
fruits= ['Bưởi', 'mango', 'Mít', 'lemon']
fruits.pop()
print(fruits) #['Bưởi', 'mango', 'Mít'] Xóa item cuối cùng

```
## Xóa Item bằng sử dụng del
```
# syntax
lst = ['item1', 'item2']
del lst[index] # 1 Item duy nhất
del lst # Xóa hoàn toàn danh sách
```

```
fruits= ['Bưởi', 'mango', 'Mít', 'lemon']
del fruits[0] # ['mango', 'Mít', 'lemon'] Xóa tại vị trí 
del fruits[1:3] #['Bưởi', 'lemon']
del fruits # NameError: name 'fruits' is not defined Không xác định được fruits
```

## Xóa item trong list
Sử dụng phương thức clear():

```
fruits= ['Bưởi', 'mango', 'Mít', 'lemon']
fruits.clear()
print(fruits) # []
``` 

## Copy list
Có thể sao chép một danh sách bằng cách gán lại cho nó một biến mới. Sử dụng phương thức copy()
```
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()

```

```
fruits= ['Bưởi', 'mango', 'Mít', 'lemon']
Hoaqua = fruits.copy()
print(Hoaqua) #['Bưởi', 'mango', 'Mít', 'lemon']
```

## Joinning List - Gộp.
```
fruits= ['Bưởi', 'mango', 'Mít', 'lemon']
Hoaqua= ['banana', 'orange', 'apple', 'lime']
Total = fruits + Hoaqua 
Tree= ['Forest']
Totals = Tree + fruits +Hoaqua

print(Totals) #['Forest:', 'Bưởi', 'mango', 'Mít', 'lemon', 'banana', 'orange', 'apple', 'lime']
```

```
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Dãy số:', num1) #Dãy số: [0, 1, 2, 3, 4, 5, 6]

fruits= ['banana', 'orange', 'apple', 'lime']
Hoaqua= ['Bưởi', 'mango', 'Mít', 'lemon']
fruits.extend(Hoaqua)
print('Liệt kê ra:',fruits)#Liệt kê ra: ['banana', 'orange', 'apple', 'lime', 'Bưởi', 'mango', 'Mít', 'lemon']

```
## Đếm item trong list
```
# syntax
lst = ['item1', 'item2']
lst.count(item)
```

## Sắp xếp danh sách
Để sắp xếp danh sách, chúng ta có thể sử dụng phương thức sort() hoặc function sorted().

### Sort()
```
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```
```
alp= ['alo', 'dog', 'boy', 'change', 'encript', 'new', 'porttal ', 'qiut', 'xxx', 'ypung', 'zilla']
alp.sort()
print(alp) #['alo', 'boy', 'change', 'dog', 'encript', 'new', 'porttal ', 'qiut', 'xxx', 'ypung', 'zilla']
alp.sort(reverse=True)
print(alp) #['zilla', 'ypung', 'xxx', 'qiut', 'porttal ', 'new', 'encript', 'dog', 'change', 'boy', 'alo']
```

### sorted()
```
alp= ['alo', 'dog', 'boy', 'change', 'encript', 'new', 'porttal ', 'qiut', 'xxx', 'ypung', 'zilla']

print(sorted(alp)) #['alo', 'boy', 'change', 'dog', 'encript', 'new', 'porttal ', 'qiut', 'xxx', 'ypung', 'zilla']
print(sorted(alp,reverse=True)) #['zilla', 'ypung', 'xxx', 'qiut', 'porttal ', 'new', 'encript', 'dog', 'change', 'boy', 'alo']

```
[<<Phần 4](../docs-tutorial-py/part4.md) [Phần 6>>](../docs-tutorial-py/part6.md)