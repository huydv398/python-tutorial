[<<Phần 7](../docs-tutorial-py/part7.md) [Phần 9>>](../docs-tutorial-py/part9.md)
# Dictionaries
Là một tập hợp các kiểu dữ liệu được ghép nối (khóa: giá trị) không có thứ tự, có thể sửa đổi (có thể thay đổi).
## Tạo Dictionaries
```
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

```

```
person = {
    'first_name':'Đường',
    'last_name':'Huy',
    'age':22,
    'country':'Vietnames',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    'address':{
        'street':'Phố cổ',
        'zipcode':'10000'
    }
    }
```

## Xóa key và value khỏi dirtionary
* `pop(key)`: Loại bỏ mục có tên key được chỉ định:
* `popitem()`: loại bỏ Item cuối cùng
* del: loại bỏ một item có tên key được chỉ định
[<<Phần 7](../docs-tutorial-py/part7.md) [Phần 9>>](../docs-tutorial-py/part9.md)