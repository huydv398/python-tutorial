[<<Phần 9](../docs-tutorial-py/part9.md) [Phần 11>>](../docs-tutorial-py/part11.md)
# Vòng lặp
Trong lập trình có việc vấn đề oahir lặp đi lập lại. Để sử lý công việc lặp đi lặp lại các ngôn ngữ lập trình cung cấp các vòng lặp.
* while
* for

## While
Nó được sử dụng để thực hiện lặp đi lặp lại một khối câu lệnh cho đến khi một kiện nhất định được thỏa mãn. Khi điều kiện sai,các dòng mã sau sau vòng lặp sẽ được tiếp tục thực hiện.

```
  # syntax
while condition:
    code goes here
```

ex:
```
sodem = 0
while sodem < 5:
    print(sodem)
    sodem = sodem + 1
```
``` 
huydv@ubuntu:~/python$ python d10.py 
0
1
2
3
4
```
Trong vòng lặp while ở trên, điều kiện trở thành sai là số đến 5. đó là khi vòng lặp dừng lại

```
while condition:
    code goes here
else:
    code goes here
```

ex:
```
sodem = 0
while sodem < 5:
    print(sodem)
    sodem = sodem + 1
else:
    print(sodem)
```

```
huydv@ubuntu:~/python$ python d10.py 
0
1
2
3
4
5
```
Điều kiện vòng lặp trên sẽ là false khi đếm đến số 5 và vòng lặp sẽ dùng lại và việc thực thi bắt đầu câu lệnh else. 
## Break and Continue - Part 1

* Break: Khi muốn thoát vòng lặp.
```
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

ex:
```
sodem = 0
while sodem < 5:
    print(sodem)
    sodem = sodem + 1
    if sodem == 3:
        break
```
output:
```
$ python d10.py 
0
1
2
```
Khi điều kiện if ==3 thì vòng lặp dừng lại.
## continue
Có thể dùng lần lặp hiện tại và tiếp tục với phần tiếp theo:
```
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

ex:
```
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
```

Output: 0,1,2,4

## Vòng lặp for
Được sử dụng để tạo ra vòng lặp, tương đương với các ngôn ngữ lập trình khác, nhưng có một số khác biệt về cú pháp. Vòng lặp được sử dụng để lặp lại một chuỗi(đó có thể là một list, tuple, dirtionary, set, string)

* vòng lặp for cho list:
```
# syntax
for iterator in lst:
    code goes here
```

```
num_list = [0, 1, 2, 3, 4, 5]
for num in num_list: 
    print('Các số là: ',num)
```

* Vòng lặp với chuỗi
```
# syntax
for iterator in string:
    code goes here
```
```
word = 'huydv'
for Show in word:
    print(Show)
```

```
$ python3 d10.py 
h
u
y
d
v
```
## Break và coutinue - part 2

Break dùng để dừng vòng lặp trước khi hoàn thành
```
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

```
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```
continue: Khi chúng  tôi muốn bỏ qua một số bước trong quá trình lặp lại của vòng lặp
```
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

```
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('số tiếp theo:  ', number + 1) if number != 5 else print("Vòng lặp kết thúc") # for short hand conditions need both if and else statements
print('Bên ngoài vòng lặp')
```
```
~/python$ python3 d10.py 
0
số tiếp theo:   1
1
số tiếp theo:   2
2
số tiếp theo:   3
3
4
số tiếp theo:   5
5
Vòng lặp kết thúc
Bên ngoài vòng lặp
```

Trong ví dụ trên, nếu số bằng 3, bước sau điều kiện(nhưng bên trong vòng lặp) sẽ bị bỏ qua và thực hiện vòng lặp continue nếu còn lại bất kỳ lần lặp nào.

## Hàm Range
Function range() sử dụng để lặp qua một bộ code một số lần nhất định. range(start,end,step) nhận 3 tham số:start, end,gia số. Theo mặc định, nó bắt đầu từ số 0 và gia số là 1. Chuỗi phạm vi cần ít nhất 1 đối số(end). Tạo trình tự sử dụng range()

```
# syntax
for iterator in range(start, end, increment):

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```
for number in range(11):
    print(number)
```
output:

```
0
1
2
3
4
5
6
7
8
9
10
```

## Vòng lặp lồng nhau
```
# syntax
for x in y:
    for t in s:
        print(t)
```
ex:
```
person = {
    'Họ':'Đường',
    'Tên':'Huy',
    'Tuổi':22,
    'Quốc gia':'Vietnames',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'nguyenngocvu',
        'zipcode':'10000'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

```
$ python3 d10.py 
JavaScript
React
Node
MongoDB
Python
```
### For else
```
# syntax
for iterator in range(start, end, increment):
    do something
else:
    print('Kết thúc vòng lặp')
```
exam:
```
for number in range(11):
    print(number)   # In số 0 to 10, not including 11
else:
    print('Vòng lặp kết thúc tại', number)
```
output
```
$ python3 d10.py 
0
1
2
3
4
5
6
7
8
9
10
Vòng lặp kết thúc tại 10
```
## Pass
Trong python khi câu lệnh được yêu cầu(sau dấu chấm phẩy), Nhưng chúng ta không muốn thực thi bất kỳ đoạn mã nào ở đó, chúng ta có thể viết từ pass để tránh qua lỗi. Ngoài ra chúng ta có thể sử dụng nó như một trình dữ chỗ, cho các câu lệnh trong tương lai.

ex:
```
for number in range(6):
    pass
```
output:
```

```
[<<Phần 9](../docs-tutorial-py/part9.md) [Phần 11>>](../docs-tutorial-py/part11.md)