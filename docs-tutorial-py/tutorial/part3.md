[<<Phần 2](../docs-tutorial-py/part2.md) [Phần 4>>](../docs-tutorial-py/part4.md)
## Boolean 
Kiểu dữ liệu Boolean đại diện cho một giá trị đúng hoặc sai. Việc sử dụng các kiểu dữ liệu này sẽ rõ ràng khi chúng ta bắt đầu sử dụng toán sử so sánh.

|Toán tử|Ví dụ|Giống như|
|-|-|-|
|=|x = 5|x=5|
|+=| x += 3|x = x + 3|
|-=|x -= 3|x = x-3|
|*= | x *= 3 | x = x*3|
|/=|x /= 3|x = x/3|
|%=|x %= 3|x = x%3|
|//=|X //= 3|X = X // 3|
|**=|X **= 3|X = X ** 3|
|&=|x &= 3|x = & 3|
|`|=`|x |= 3|x = x | 3|
|^=| x ^= 3|x = x ^ 3|
|>>=|X >>= 3|X = >> 3|
|<<=|X <<= 3| X = X << 3|

```
>>> print('Complex number: ', 1+1j)
Complex number:  (1+1j)
>>> print('Multiplying complex numbers: ',(1+1j) * (1-1j))
Multiplying complex numbers:  (2+0j)
```

|Toán tử|tên|ví dụ|
|-|-|-|
|==|bằng nhau|a == b|
|!=|Không bằng nhau|a != b|
|>|Lớn hơn|a > b|
|<|Nhỏ hơn|a < b|
|<=|Hơn hoặc bằng|a <= b|
|>=|Lớn hơn hoặc bằng|a >= b|

Toán tử so sánh
```
>>> print(3 > 2)
True
>>> print(3 >= 2)
True
>>> print(2 <= 3)
True
>>> print(len('mango') == len('avocado'))
False
>>> print(len('milk') != len('meat'))
False
>>> print(len('tomato') == len('potato'))
True

# so sánh cái gì đó đúng hoặc sai
>>> print('True == True: ', True == True)
True == True:  True
>>> print('True == False: ', True == False)
True == False:  False
>>> print('False == False:', False == False)
False == False: True
>>> print('True and True: ', True and True)
True and True:  True
>>> print('True or False:', True or False)
True or False: True
```

Toán tử logic:
```
print(3 > 2 and 4 > 3) # True - vì cả hai câu lệnh đều là true
print(3 > 2 and 4 < 3) # False - vì câu lệnh thứ hai là  false
print(3 < 2 and 4 < 3) # False - vì cả hai câu lệnh đều  false
print(3 > 2 or 4 > 3)  # True -vì cả hai câu lệnh đều true
print(3 > 2 or 4 < 3)  # True -vì một trong các câu lệnh là true
print(3 < 2 or 4 < 3)  # False -vì cả hai câu lệnh đều false
print(not 3 > 2)     #False   vì 3> 2 là true, sau đó không True cho False
print(not True)      # False - Phủ định, toán tử not chuyển true thành false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```
[<<Phần 2](../docs-tutorial-py/part2.md) [Phần 4>>](../docs-tutorial-py/part4.md)