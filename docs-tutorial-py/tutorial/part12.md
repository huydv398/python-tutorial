[<<Phần 11](../docs-tutorial-py/tutorial/part10.md) [Phần 12>>](../docs-tutorial-py/tutorial/part13.md)
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
* `math`(toán học)
* `datetime`(ngày giờ)
* `os`(hệ điều hành)
* `sys`(hệ thống)
* `random`(ngẫu nhiên)
* `statistics`(thống kê)
* `collections`(tập hợp, thu thập)
* `json`
* `re`

## OS Module
Có thể tự động thực hiện tác vụ của hệ điều hành. OS module cung cấp các chức năng để tạo, thay đổi thư mục làm việc hiện tại và xóa thư mục(folder), Tìm nạp nội dung của nó, thay đổi xác định thư mục hiện tại.

## Sys module
Cung cấp các hàm và biến được sử dụng để thao tác các phần khác nhau của môi trường thời gian chạy Python. Function sys.argv trả về các danh sách đối số dòng lệnh, tại chỉ mục 1 là đối số được truyền từ dòng lệnh.

## Statistics Module
Cung cấp các function để thống kê toán học của dữ liệu số. các function thống kê phổ biến được định nghĩa trong module này: mean, median, mode, stdev,v.v.

## Math Module
Module chứa nhiều phép toán và hằng số.

# String Module
Một mô-đun hữu ích cho nhiều mục đích. Dưới đây là một ví dụ về chuỗi mà chúng tôi có thể lấy từ nó.
## Random Module
Bây giờ bạn đã quen với việc nhập các mô-đun. Hãy thực hiện thêm một lần nhập nữa để làm quen với nó. Hãy nhập mô-đun ngẫu nhiên cho chúng ta một số ngẫu nhiên từ 0 đến 0,9999 .... Mô-đun ngẫu nhiên có rất nhiều chức năng nhưng trong phần này chúng tôi sẽ chỉ sử dụng random và randint .