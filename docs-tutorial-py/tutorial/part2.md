
[<<Phần 1](docs-tutorial-py/tutorial/part1.md) [Phần 3>>](docs-tutorial-py/tutorial/part3.md)
# Chức năng tích hợp sẵn
Trong python, chúng tôi có rất nhiều chức năng được tích hợp sẵn. Các chức năng tích hợp sẵn trên toàn cầu để bạn sử dụng. Một hàm tích hợp trong Python được sử dụng phổ biến như sau
* `print ()` 
* `len ()` 
* `type () `
* `int () `
* `float () `
* `str ()` 
* `input ()` 
* `list ()` 
* `dict ()` 
* `min ()` 
* `max ()` 
* `sum ()` 
* `sorted ()` 
* `open ()` 
* `file ()` 
* `help ()`
* `dir ()`

![](../image/i1.png)

Sử dụng một số hàm phổ biến:
```
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                
```
Các keyword phổ biến của python

## Biến variables
Các biến lưu trữ dữ liệu trong bộ nhớ máy tính. Các biến ghi nhớ được khuyến khích sử dụng trong nhiều ngôn ngữ lập trình. Một biến đề cập đến một địa chỉ bộ nhớ trong đó dữ liệu đang được lưu trữ. Quy tắc trong Python:
* Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới
* Tên biến không thể bắt đầu bằng số
* Tên biến chỉ có thể chứa các ký tự- số và dấu gạch dưới(Aa, 0-9 và _)
* Tên biến có phân biệt hoa thường

Ví dụ:
```
# Biến trong Python

first_name = 'Đường'
last_name = 'Huy'
country = 'Vietnam'
city = 'Hanoi'
age = 23
is_married = False
skills = ['1', '2', '3', '4', 'Python']
person_info = {
   'firstname':'Đường',
   'lastname':'Huy',
   'country':'Vietnam',
   'city':'HanoiSS'
   }

```
```
>>> first_name = 'Đường'
>>> last_name = 'Huy'
>>> country = 'Vietnam'
>>> city = 'Hanoi'
>>> age = 23
>>> is_married = False
>>> skills = ['1', '2', '3', '4', 'Python']
>>> person_info = {
...    'firstname':'Đường',
...    'lastname':'Huy',
...    'country':'Vietnam',
...    'city':'HanoiSS'
...    }
>>> print('Họ và tên:', first_name, last_name)
Họ và tên: Đường Huy
>>> print('Độ dài của Họ:', len(first_name))
First name length: 5
>>> print('Quốc gia: ', country)
Quốc gia:  Vietnam
>>> print('Tuổi: ', age)
Tuổi:  23
>>> print('Tình trạng hôn nhân: ', is_married)
Tình trạng hôn nhân:  False
```

Nhập thông tin của người dùng bằng cách tích hợp hàm `input()`. Hãy gán dữ liệu chúng nhận được từ người dùng vào các biến first_name và age. Ví dụ:
```
>>> first_name = input('Tên của bạn là gì: ')
What is your name: Đường Văn Huy
>>> age = input('Bạn bao nhiêu tuổi? ')
How old are you? 23
>>> print('Họ và tên:',first_name)
Họ và tên: Đường Văn Huy
>>> print(age)
23
```

## Loại dữ liệu
Có một số kiểu dữ liệu trong Python. Để xác định kiểu dữ liệu, sử dụng hàm `type()`
## Casting
Chuyển đổi một kiểu dữ liệu này sang kiểu dữ liệu khác. Chúng ta sử dụng int(), float(), str(), list. Khi thực hiện các phép toán số học, đầu tiên chuỗi số nên được chuyển đổi thành `int` hoặc `float`, nếu không nó sẽ trả về một lỗi. Nếu chúng ta nối một số chuỗi, trước tiên số đó phải được chuyển thành chuỗi. 

```
# đặt biến num_int =10
>>> num_int = 10
>>> print('Số nguyên là:',num_int) 
Số nguyên là: 10
# Chuyển đổi biến num_int thành kiểu float
>>> num_float = float(num_int)

# In biến 
>>> print('Biến float:', num_float)
Biến float: 10.0

# Chuyển đổi từ float -> int
>>> num=10.234
>>> print(in)  
>>> print(int(num))
10

# str to int

num_str ='12.23'

```
```
>>> first_name = 'Đường Văn Huy'
>>> print(first_name)
Đường Văn Huy
>>> first_name_to_list = list(first_name)
>>> print(first_name_to_list)
['Đ', 'ư', 'ờ', 'n', 'g', ' ', 'V', 'ă', 'n', ' ', 'H', 'u', 'y']
```

[<<Phần 1](docs-tutorial-py/tutorial/part1.md) [Phần 3>>](docs-tutorial-py/tutorial/part3.md)