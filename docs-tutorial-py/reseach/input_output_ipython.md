# Nhập xuất trong Python
## Hàm print
* Hàm print giúp xuất các nội dung mà người dùng muốn ra shell
* cú pháp
```
print(*object, sep='', end='\n', file=sys.stdout, flush=False)
```
## Giới thiệu IPython
* Cài đặt IPython
```
pip3 install ipython
```

* Ví dụ về tương tác phiên:
```
def say(name):
    print('hello {in_name}'.format(in_name=name))

say('huydv') #hello huydv
```

### Lệnh hữu ích nhất
Bốn lệnh hưu ích nhất, cũng như mô tả ngắn ngọn của chúng, được hiển thị cho bạn trong một biểu ngữ, mỗi khi sử dụng Python:
* `?`: giới thiệu và tổng quan về các tính năng của Python
* `%quickref`:  Tài liệu Quick
* `help`: Hệ thống trợ giúp của riêng Python.
* `object?`: Thông tin chi tiết về ‘`object`’, sử dụng ‘`object ??`’ để biết thêm chi tiết.
