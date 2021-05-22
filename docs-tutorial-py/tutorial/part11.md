[<<Phần 10](../docs-tutorial-py/part10.md) [Phần 12>>](../docs-tutorial-py/part12.md)
# Function
Chức năng- chúng ta thấy nhiều hàm python được tích hợp sẵn. Trong phần này, chúng tôi sẽ tập trung vào các function tùy chỉnh. Function là gì? Trước khi tạo Function, Chúng ta tìm hiểu hàm là gì và tại sao chúng ta cần chúng?

## Xác định một Function
Funtion là một khối mã có thể sử dụng lại hoặc các câu lệnh lập tình được thiết kế để thực hiện một tác vụ nhất định. Để định nghĩa một hàm, Python cung cấp key `def`. Sau đây là cú pháp để xác định một hàm. Block code Function chỉ được thực thi khi chúng ta gọi nó.

## Khai báo và gọi một hàm
Chúng ta tạo ra một hàm(Khai báo Function). Khi bắt đầu sử dụng nó. Khi bắt đầu sử dụng, calling hoặc kêu gọi hàm. Hàm có thể được khai báo có hoặc không có tham số.
```
# syntax
# Khai báo 1 function
def function_name():
    codes
    codes
# Calling a function
function_name()
```

## Function không có tham số
```
def Myname ():
    Ho = 'Đường'
    Tên = 'Huy'
    space = ' '
    full_name = Ho + space + Tên
    print(full_name)
Myname () # Gọi function

def tong ():
    so1 = 2
    so2 = 3
    total = so1 + so2
    print(total)
tong()
```
## Function trả lại giá trị Part 1
Function cũng có thể trả về giá trị, nếu một hàm không trả về giá trị nào thì giá trị của hàm là None. Cho phép viết lại các function trên bằng `return`. Từ bây giờ, ta nhận được một giá trị khi gọi hàm, thay vì in nó.

```
def myname ():
    ho = 'Duong'
    ten = 'huy'
    space = ' '
    full_name = ho + space + ten
    return full_name
print(myname())
```
output: Duong huy
## Function với tham số
Trong một hàm, chúng ta có thể chuyển các kiểu dữ liệu khác nhau(số, chuỗi, boolean, list, tuple, dirtionary, set)dưới dạng tham số

* Tham số đơn: Nếu hàm của chúng ta nhận một số, chúng ta nên gọi hàm của mình bằng một đối số.

```
# syntax
  # Khai báo một hàm
  def function_name(parameter):
    codes
    codes
  # Calling function
  function_name(parameter)
```

```
print(greetings('huydv')) #huydv, Chào mừng bạn đến với python!!

def congthem10 (so):
    muoi =10
    return so + muoi
print(congthem10(1)) #11

def canhvuong(x):
    return x * x
print('S hình vuông: ', canhvuong(3))

def tổng(n):
    total = 0
    for i in range(n +1): # range xuất phát từ 0.1-4 phải cộng thêm 1
        total +=i
    print(total)# cộng dồn tại đây
tổng(4) #10 1+2+3+4
```

* Hai tham số: Một function có thể có hoặc không có tham số hoặc các tham số. Một hàm có thể có hai hoặc nhiều tham số. Nếu hàm của chúng ta nhận tham số, chúng ta nên gọi nó với các đối số. Hãy kiểm tra một hàm với hai tham số.

```
  # syntax
  # Khai báo 1 function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  function_name(arg1, arg2)
```

```
def myfullname (ho, ten):
    space = ' '
    hoten = ho + space + ten
    return hoten
print('Họ tên của tui: ', myfullname('duong', 'huy')) #Họ tên của tui:  duong huy

def tong (so1, so2):
    total = so1 + so2
    return total
print('tổng của 2 số: ',tong(2, 5))#tổng của 2 số:  7

def tinhtuoi(namsinh):
    tuoi = 2021 -namsinh
    return tuoi
print('tuổi của tôi là: ',tinhtuoi(1998))#tuổi của tôi là:  23
```
## Passing Arguments with Key and Value
Nếu chúng ta truyền các đối số có key và giá trị, thứ tự của các đối số không quan trọng.
```
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
function_name(para1='John', para2='Doe') #Thứ tự của các đối số không quan trọng ở đây
```

```
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname='Asabeneh', lastname='Yetayeh')
```

## Function Returning a Value
Hàm sẽ trả về none theo mặc định nếu chúng ta cho cho value cho hàm. Để trả về một giá trị bằng một hàm, chúng ta sử dụng key return theo sau là biến mà chúng ta đang muốn trả về. Chúng ta có thể trả về bất kỳ loại kiểu dữ liệu nào từ một funtion
### Returning a boolean: 
```
def chanle (n):
    if n%2 ==0:
        return "chẵn"
    return "lẻ"
print(chanle(5))# lẻ
print(chanle(6))# chẵn
```
### Returning a list:
```
def timso(n):
    listd=[]
    for i in range(n+1):
        if i % 4 ==0:
            listd.append(i)
    return listd
print(timso(13)) # n=13 thì i chạy từ 0-13. nếu i chia hết cho 4 lấy số i thêm vào list
```
output: [0, 4, 8, 12]
## Function with Default Parameters

Đôi khi cúng ta chuyển các giá trị mặc định cho các tham số, khi chúng ta gọi hàm. Nếu chúng ta không truyền các đối số khi gọi hàm, các giá trị mặc định của chúng ta sẽ được sử dụng.

```
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

```
def hoten (ho = 'Nguyen'):
    spa=' '
    name= ho +spa+ ":là họ của tôi"
    return name
print(hoten())#Nguyen :là họ của tôi
print(hoten ('Duong'))#Duong :là họ của tôi

def hoten(ho='Họ', ten='và Tên?'):
    spa=' '
    name = ho +spa+ ten
    return name
print(hoten())#Họ và Tên?
print(hoten('Duong','Huy'))#Duong Huy
```

## Đối số tùy chỉnh
Nếu chúng ta không biết số lượng đối số mà chúng ta truyền vào function của mình, chúng ta có thể tạo một hàm có thể nhận số lượng đối số tùy ý bằng cách thêm * vào trước tên tham số
```
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

```
def mem (nhom,*member):
    print(nhom)
    for i in member:
        print(i)
# mem ('Nhóm RD','Huy', 'Huy2', 'Huy3', 'Huy4')
```
output:
```
Nhóm RD
Huy
Huy2
Huy3
Huy4
```
## Số lượng tham số mặc định và tùy ý trong hàm
```
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))
```
[<<Phần 10](../docs-tutorial-py/part10.md) [Phần 12>>](../docs-tutorial-py/part12.md)