## Xuống dòng trong mệnh đề
* Một lệnh hoặc một mệnh đề trong code thường kết thúc khi xuống dòng mới. Tuy nhiên, trong Python, có thể dùng dấu `\` để tiếp tục lệnh hoặc mệnh đề tiếp theo:
```
total = 1 +\
        20 + \
        32
print(total) #53
```
Hoặc 
```
total = item1 + item2 + item3
```

Những mệnh đề có chứa dấu `{}`, `[]`, `()` thì không cần sử dụng `\` nếu muốn xuống dòng trong các dấu ngoặc.
## Quotation trong Python
```
word = 'word'
sentence = "This is a sentence."
paragraph = """Chuỗi văn bản dùng dấu 3 dấu có thể
enter xuống dòng mà python vẫn hiểu nghĩa"""
```

## Command trong py
* SỬ dụng hash `#` mà khong ở trong 1 chuỗi thì sẽ bắt đầu  cho 1 comment (trên một dòng)

```
# /usr/bin/python

# Comment
print ("Hello my love!) # In ra chuỗi
```

Hoặc

```
'''
Những đoạn bên trong sẽ được comment lại
line2
line3
```

### Chạy nhiều lệnh trên cùng 1 dòng :
* Sử dụng dấu ; để ngăn cách giữa các lệnh :
```
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```

## Kiểu dữ liệu
Trong Python hỗ trợ rất nhiều kiểu dữ liệu số (*numeric*) . Một số kiểu dữ liệu cơ bản như số nguyên ( *integer* ) , số thực ( *floating-point* ) , phân số ( *fraction* ) , số phức ( *complex* ) ,

### Phân số
Để tạo một phân số(Fraction) trong python, sử dụng hàm Fraction với cú pháp:
```
Fraction(tử_số, mẫu_số)
```

