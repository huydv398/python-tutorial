[<<Phần 8](../docs-tutorial-py/tutorial/part8.md) [Phần 10>>](../docs-tutorial-py/tutorial/part10.md)
## Điều kiện
Theo mặc định, các câu lệnh trong python được thực thi tuần tự từ trên xuống dưới. Nếu logic xử lý yêu cầu như vậy, Luồng thực thi tuần tự có thể được thay đổi theo 2 cách
* Thực thi có điều kiện: Một khối gồm một hoặc nhiều câu lệnh sẽ được thực hiện Nếu một biểu thức nhất định là đúng.
* Thực thi lặp đi lặp lại: Một khối gồm một hoặc nhiều câu lệnh sẽ được thực hiện lặp đi lặp lại miễn là một biểu thức nào đó là đúng. Trong phần này, Chúng ta sẽ đề cập đến câu lệnh if, else, elif. Các phần tử toán học trong các trước sẽ hữu ích ở đây
## If Condition

Trong Python và các ngôn ngữ lập trình khác, từ khóa if chúng ta sử dụng để kiểm tra xem một điều kiện có đúng không và để thực thi block code. 
```
# syntax
if condition:
    Sẽ chạy code ở đây nếu điều kiện là đúng
```

Tuy nhiên nếu điều kiện sai, chúng ta không thấy kết quả. Để xem kết quả của điều kiện sai, chúng ta có thêm một khối khác.

## If Else
Điều kiện If là đúng, khối đầu tiên được thực hiện, nếu sai, Điều kiện else sẽ được thực thi:
```
#syntax
if condition:
    Đúng, Chạy lệnh ở đây
else:
    Nếu không chạy lệnh này
```
Example:
```
a = 3
if a>0:
    print('Điều kiện if là đúng.')
else:
    print('Thực hiện lệnh ở else.')
```
Output: Điều kiện if là đúng.


```
a = -1
if a>0:
    print('Điều kiện if là đúng.')
else:
    print('Thực hiện lệnh ở else.')
```
Output: Thực hiện lệnh ở else.

## If elif else
Sử dụng elif khi có nhiều điều kiện:

```
# syntax
if condition:
    code
elif condition:
    code
else:
    code
```

ex
```
a = 0
if a  >0:
    print('số lớn hơn 0')
elif a < 0:
    print("số nhỏ hơn 0")
else:
    print('số bằng 0')
```
## Short Hand
```
# syntax
code if condition else code
```

```
a = 3
print('Là một số dương') if a >0 else print('là một số âm')
```
Output: Là một số dương

## Điều kiện lồng nhau

```
# syntax
if condition:
    code
    if condition:
    code
```

```
a =11
if a > 0:
    if a % 2 == 0:
        print('a là một số nguyên dương và là số chẵn')
    else:
        print('a là một số lẻ')
elif a == 0:
    print('a bằng 0')
else:
    print('a là số âm')
```
output: a là một số lẻ

Chúng ta có thể tránh viết điều kiện lồng nhau bằng việc sử dụng toán tử là logic.

## Điều kiện If và toán tử logic
```
# syntax
if condition and condition:
    code
```

```
a = 14
if a > 0 and a % 2 == 0:
        print('a -số nguyên -chẵn')
elif a > 0 and (a % 2) != 0:
     print('a- số nguyên')
elif a == 0:
    print('a = 0')
else:
    print('a số âm')
```
Output: a -số nguyên -chẵn

## Toán tử or and

```
# syntax
if condition or condition:
    code
```

ex1:
```

user = 'Huydv'
level = 3
if user == 'admin' or level >= 4:
        print('Cho phép!')
else:
    print('Không cho phép!')
```
output: Không cho phép!

```
user = 'Huydv'
level = 6
if user == 'admin' or level >= 4:
        print('Cho phép!!')
else:
    print('Không cho phép!')
```
output: Cho phép!!(level =6>=4)

```
user = 'admin'
level = 1
if user == 'admin' or level >= 4:
        print('Cho phép!!')
else:
    print('Không cho phép!')
```
output: Cho phép!!(user == admin)


toán tử **and**
```
user = 'admin'
level = 6
if user == 'admin' and level >= 4:
        print('Cho phép!!')
else:
    print('Không cho phép!')

```
output:     Cho phép!!
## sd
[<<Phần 8](../docs-tutorial-py/tutorial/part8.md) [Phần 10>>](../docs-tutorial-py/tutorial/part10.md)