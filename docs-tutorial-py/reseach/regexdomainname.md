# Quy cách tạo một domain    
Một miền phải tuân theo các quy tắc dưới đây:

* Tên miền phải là az | AZ | 0-9 và dấu gạch ngang (-)
* Tên miền phải dài từ 1 đến 63 ký tự
* Tld cuối cùng phải có ít nhất hai ký tự và tối đa là 6 ký tự
* Tên miền không được bắt đầu hoặc kết thúc bằng dấu gạch ngang (-) (ví dụ: -google.com hoặc google-.com)
* Tên miền có thể là một miền phụ (ví dụ: mkyong.blogspot.com)

```
import re
valid_domains = """
www.google.com
google.com
mkyong123.com
mkyong-info.com
sub.mkyong.com
sub.mkyong-info.com
mkyong.com.au
g.co
mkyong.t.t.co
"""

invalid_domains = """
mkyong.t.t.c
mkyong,com
mkyong
mkyong.123
.com
mkyong.com/users
-mkyong.com
mkyong-.com
sub.-mkyong.com
sub.mkyong-.com
"""
# Tách valid_domains thành list
valid_names = valid_domains.split()
print(valid_names)
## Output:['www.google.com', 'google.com', 'mkyong123.com', 'mkyong-info.com', 'sub.mkyong.com', 'sub.mkyong-info.com', 'mkyong.com.au', 'g.co', 'mkyong.t.t.co']

# Tách invalid_names thành list
invalid_names = invalid_domains.split()
print(invalid_names)
## Output: ['mkyong.t.t.c', 'mkyong,com', 'mkyong', 'mkyong.123', '.com', 'mkyong.com/users', '-mkyong.com', 'mkyong-.com', 'sub.-mkyong.com', 'sub.mkyong-.com']


# match 1 character domain name or 2+ domain name


pattern = '^([A-Za-z0-9]\.|[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]\.){1,3}[A-Za-z]{2,6}$'

print( 'Các tên miền bên dưới là đúng quy cách ============')
for name in valid_names:
    print( name.ljust(50), ('True' if re.match(pattern, name) else 'False').rjust(5))

print( '\nCác tên miền bên dưới sai quy cách ============')
for name in invalid_names:
    print (name.ljust(50), ('True' if re.match(pattern, name) else 'False').rjust(5))

domain = 'ôkjffie.com'
if re.match(pattern, domain):
    print('true')
else:
    print('false')