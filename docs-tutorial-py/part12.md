[<<Phần 11](../docs-tutorial-py/part10.md) [Phần 12>>](../docs-tutorial-py/part13.md)
# Module
## Module là gì?
Là một tệp chứa một bộ code hoặc một bộ Function có thể được đưa vào một ứng dụng. Module có thể là một tệp chứa một biến duy nhất hoặc một hàm, một code base lớn.

## Tạo một Module
Để tạo một Module, viết mã trong một tệp python và nó lưu dưới dạng **mymodule.py**. 

Ở đây tôi tạo tên file là d12.py
```
#d12.py
def hoten(ho, ten):
    spa=' '
    hoten = ho +spa+ ten
    return hoten

```
## Import module
```
#d12main.py
import d12
print(d12.hoten('duong','huy'))
```

Uotput:
```
$ python3 d12main.py 
duong huy
```

## Import function từ module
Chúng tôi có thể có nhiều function trong 1 tệp và có thể nhập tất cả các function theo cách khác nhau.

```
#d12main.py
import d12
print(d12.hoten('duong','huy'))

from d12 import hoten , congthem10, canhvuong ##import các function từ d12 vào
print(hoten('duong','huy'))
print(congthem10(23))
print('S hình vuông: ', canhvuong(3))
```
### Import Built-in Modules
Chúng ta cũng có thể nhập các module bằng cách nhập tên file/function bằng cách `import` keyword. Hãy import module mà chúng ta sẽ sử dụng hầu hết thời gian. Một số module tích hợp sẵn phổ biến:
* math(toán học)
* datetime(ngày giờ)
* os(hệ điều hành)
* sys(hệ thống)
* random(ngẫu nhiên)
* statistics(thống kê)
* collections(tập hợp
* thu thập)
* json
* re