[<<Phần 3](../docs-tutorial-py/part3.md) [Phần 5>>](//docs-tutorial-py/part5.md)
# Chuỗi

## String
Văn bản là một kiểu dữ liệu string. Bất kỳ kiểu dữ liệu nào được viết dưới dạng văn bản đều được  gọi là string. Bất kỳ dữ liệu nào dưới dấu nháy đơn hoặc nháy kép đều là chuỗi. Có các phương thức chuỗi khác nhau và  các hàm tích hợp để xử lý chuỗi, hãy xử lú các kiểu dữ liệu chuỗi. Để kiểm tra độ dài của một chuỗi, hãy sử dụng phương thức `len()`


## Nối chuỗi
```
first_name = 'Đường Văn'
last_name = 'Huy'
space = ' '
full_name = first_name  +  space + last_name
print(full_name)
```

## Trình tự thoát trong chuỗi
Trong python và các ngôn ngữ lập trình khác `\` theo sao là một ký tự.
* `\n`: Dòng mới
* `\t`: một dấu tab- 8 ký tự khoảng trắng
* `\\`: Dấu gạch chéo
* `\'`: Dấu ngoặc kép
* `\"`: Dấu ngoặc đơn

```

print('Hôm nay trời thật là đẹp.\nThôi đi ngủ nhỉ ?') # line break
print('Days\Bữa ăn\số tiền')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('Đây là dấu gạch chéo (\\)') # To write a backslash
print('Tại đây in ra có dấu nháy đôi \"Hello, World!\"')
```

output:
```
root@ubuntu:/home/huydv/python/d4# python3 docs.py 
Hôm nay trời thật là đẹp.
Thôi đi ngủ nhỉ ?
Days\Bữa ăn\số tiền
Day 1   3       5
Day 2   3       5
Day 3   3       5
Day 4   3       5
Đây là dấu gạch chéo (\)
Tại đây in ra có dấu nháy đôi "Hello, World!"
```

## Định dạng chuỗi

* %s - String (hoặc bất kỳ đối tượng nào có biểu diễn chuỗi, như số)
* %d - Số nguyên
* %f - Số float
* %.f - Số float với độ chính xác cố định
```
first_name = 'duong'
last_name = 'Huy'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(last_name,first_name,  language)
print(formated_string)

Output:
I am Huy duong. I teach Python
```

%(last_name,first_name,  language) Thứ tự hiển thị xủ $s

* `challenge.capitalize()`: Viết hoa chữ cái đầu tiên
* `count()`: trả về số lần xuất hiện của chuỗi con trong chuỗi, đếm
* `endwith()`: Kiểm tra xem một chuỗi có kết thúc bằng một phần cuối được chỉ định hay không
* `expandtabs()`: Thay thế ký tự tab bằng dấu cách, kích thước tab mặc định là 8. Nó nhận đối số kích thước tab
* `find()`: Trả về chỉ số thấp nhất của lần xuất hiện đầu tiên của một chuỗi con, nếu không tìm thấy thì trả về -1
* `rfind()`: Trả về chỉ số cao nhất của lần xuất hiện đầu tiên của một chuỗi con, nếu không tìm thấy thì trả về -1
* `format()`: định dạng chuỗi thành đầu ra đẹp hơn
Thông tin thêm về định dạng chuỗi, hãy kiểm tra liên kết này
* `index()`: Trả về chỉ số thấp nhất của một chuỗi con, các đối số bổ sung cho biết chỉ số bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi - 1)
* `rindex()`: Trả về chỉ số cao nhất của một chuỗi con, các đối số bổ sung cho biết chỉ số bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi - 1)
* `isalnum()`: Kiểm tra ký tự chữ và số
isalpha(): Kiểm tra xem tất cả các phần tử chuỗi có phải là ký tự bảng chữ cái hay không (az và AZ)
* `isdecimal()`: Kiểm tra xem tất cả các ký tự trong chuỗi có phải là số thập phân (0-9) không
* `isdigit()`: Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số không (0-9 và một số ký tự unicode khác cho các số)
* `isnumeric(`): Kiểm tra xem tất cả các ký tự trong một chuỗi là số hoặc có liên quan đến số (giống như isdigit(), chỉ cần chấp nhận nhiều ký hiệu hơn, như ½)
* `isidentifier()`: Kiểm tra giá trị nhận dạng hợp lệ - có nghĩa là nó kiểm tra, nếu một chuỗi là tên biến hợp lệ
* `islower()`: Kiểm tra xem tất cả các ký tự bảng chữ cái trong chuỗi có phải là chữ thường không
* `isupper()`: Kiểm tra xem tất cả các ký tự bảng chữ cái trong chuỗi có phải là chữ hoa không
* `join()`: Trả về một chuỗi được nối
* strip(): Loại bỏ tất cả các ký tự đã cho bắt đầu từ cầu xin và kết thúc của chuỗi
* `Replace()`: Thay thế chuỗi con bằng một chuỗi đã cho
* `split()`: Tách chuỗi, sử dụng chuỗi đã cho làm dấu phân tách
* `title()`: Trả về một chuỗi in nghiêng tiêu đề
* `swapcase()`: Chuyển đổi tất cả các ký tự chữ hoa thành chữ thường và tất cả các ký tự chữ thường thành các ký tự chữ hoa
* `startwith()`: Kiểm tra xem chuỗi có bắt đầu bằng chuỗi được chỉ định hay không

[<<Phần 3](../docs-tutorial-py/part3.md) [Phần 5>>](//docs-tutorial-py/part5.md)