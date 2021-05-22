# File handling
Lưu trữ dữ liệu của mình ở các dạng tệp khác nhau. Ngoài việc xử lý tệp, chúng ta cũng sẽ thấy các định dạng tệp khác nhau(.txt,.json, .xml, .csv, .tsv, .excel)

Xử lý tệp là một phần import của lập trình cho phép create, read, update and delete files.

```
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

```
* `r`-read: Mở tệp để đọc, lỗi nếu tệp không tồn tại.
* `a`- Append: mở tệp để bổ sung, tạo tệp nếu tệp đó không tồn tại.
* `w`- write: Mở tệp để ghi, tạo tệp nếu tệp đó không tồn tại
* `x` - Create  - Tạo tệp được chỉ định, trả về lỗi nếu tệp
* `t`- text : chế độ văn bản
* `b`- Binary - Chế độ nhị phân

Có một cách mới để mở tệp bằng cách sử dụng - tự đóng tệp
```
with open('/home/huydv/python/file.txt') as f:

    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

```

## Mở tệp để viết và cập nhật
Để ghi vào một tệp hiện có, chúng ta phải thêm một chế độ làm tham số cho hàm `open()`
* `a`- append :sẽ nối vào cuối tệp, nếu tệp không tồn tại, nó sẽ gây ra FileNotFoundError.
* `w` - write - sẽ ghi đè lên bất kỳ nội dung hiện có nào, nếu tệp không tồn tại thì nó sẽ tạo ra.
Ví dụ 1:
```
with open('/home/huydv/python/file1', 'a') as f:
    f.write('Đây là văn bản được thêm mới')
```
output:
```
~/python$ cat file1
Đây là văn bản được thêm mới
```
Ví dụ 2: đề lên bất kỳ nội dung hiện có nào, nếu tệp không tồn tại, tạo file
```
with open('/home/huydv/python/file1', 'a') as f:
    f.write('Văn bản này sẽ được viết trong một tập tin mới')

```

## Deleting Files
Xóa bằng module `os`
```
import os
os.remove('/home/huydv/python/file')
```

Nếu tệp không tồn tại, sẽ gây lỗi:
```
    os.remove('/home/huydv/python/file')
FileNotFoundError: [Errno 2] No such file or directory: '/home/huydv/python/file'
```

## File Types
### Tệp có Phần mở rộng txt
Tệp có phần mở rộng txt là một dạng dữ liệu rất phổ biến và chúng ta đã trình bày trong phần trước. Hãy chuyển sang tệp JSON
### Tệp có Phần mở rộng json
JSON là viết tắt của JavaScript Object Notation. Trên thực tế, đó là một đối tượng JavaScript được chuỗi hóa.

```
# dictionary
person_dct= {
    "name":"Huy",
    "country":"Vietnam",
    "city":"hanoi",
    "skills":["os", "server","sys"]
}

# JSON: A string form a dictionary
person_json= "{'name': 'Huy', 'country': 'Vietnam', 'city': 'hanoi', 'skills': ['os', 'server', 'sys']}"

# Sử dụng 3 dấu ngoặc kép để làm cho nó nhiều dòng dễ đọc

person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

## Changing JSON to Dictionary
Đầu tiên phải nhập module json và sử dụng phương thức `loads`

## Changing Dictionary to JSON

Đầu tiên phải nhập module json và sử dụng phương thức `dumps `

## Saving as JSON File
có thể lưu dữ liệu của mình dưới dạng tệp json. Hãy lưu nó dưới dạng tệp json bằng các bước sau.

```
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('/home/huydv/python/example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```
output:
```
/python$ cat example.json 
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
```
chúng tôi sử dụng mã hóa và thụt đầu dòng. Thụt lề giúp dễ đọc tệp json.
## Tệp có Phần mở rộng csv
CSV- comma separated values: các giá trị được phân tách bằng dấu phẩy. một định dạng tệp đơn giản được sử dụng để lưu trữ dữ liệu dạng bảng, chẳng hạn như bảng tính hoặc cơ sở dữ liệu. CSV là một định dạng dữ liệu rất phổ biến trong  data science- khoa học dữ liệu.

## Tệp có Phần mở rộng xlsx
Để đọc các tệp excel, chúng ta cần cài đặt gói **xlrd**.
## Tệp có phần mở rộng xml
Một định dạng dữ liệu có cấu trúc khác trông giống như HTML. Trong XML, các thẻ không được xác định trước. Dòng đầu tiên là một khai báo XML.
```
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>

```