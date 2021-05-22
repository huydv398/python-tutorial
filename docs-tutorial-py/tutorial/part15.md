# Higher Order Functions
Trong python các function được coi là class cao nhất, cho phép bạn thực hiện các thao tác sau trên hàm:

* Một hàm có thể nhận một hoặc nhiều hàm làm tham số
* Một hàm có thể được trả về do kết quả của một hàm khác.
* Một function có thể được sửa đổi
* Một hàm có thể được gán cho một biến
Trong phần này, chúng tôi sẽ đề cập đến:
* Sử lý các function dưới dạng tham số
* trả về các hàm dưới dạng giá trị trả về từ các hàm khác
* Sử dụng  closures and decorators trong python

## Function as a Parameter
# Python Closures
Python cho phép một hàm lồng nhau truy cập vào phạm vi bên ngoài của hàm bao quanh. Điều này được gọi là Closures. Hãy xem cách Closures hoạt động trong Python. Trong Python, bao đóng được tạo bằng cách lồng một hàm bên trong một hàm đóng gói khác và sau đó trả về hàm bên trong. Xem ví dụ bên dưới.

## Python - Map Function
một hàm tích hợp có một hàm và có thể lặp lại làm tham số.
```
    # syntax
    map(function, iterable)
```

## Python - Filter Function

gọi hàm được chỉ định trả về boolean cho mỗi mục của danh sách có thể lặp lại được chỉ định. Nó lọc các mục đáp ứng các tiêu chí lọc.
```
    # syntax
    filter(function, iterable)
```

## Python - Reduce Function
được định nghĩa trong mô-đun functools và chúng ta nên nhập nó từ mô-đun này. Giống như bản đồ và bộ lọc, nó có hai tham số, một hàm và một có thể lặp lại. Tuy nhiên, nó không trả về một giá trị có thể lặp lại khác, thay vào đó nó trả về một giá trị duy nhất

## Python Error Types
Khi viết mã, thường mắc lỗi chính tả và một số lỗi phổ biến khác nhau. Nếu mã không chạy được, python sẽ hiển thị một thông báo, chứa phản hồi thông về vị trí xảy ra sự cố loại lỗi. Đôi khi nó cũng cung cấp cho đề xuất về cách khác phục có thể. Hiểu các loại lỗi khác nhau trong ngôn ngữ lập trình sẽ giúp gỡ lỗi code của mình một cách nhanh chóng và nó cũng giúp làm tốt hơn.

## SyntaxError

```
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```
## NameError
```
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```