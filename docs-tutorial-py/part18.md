# Regular Expressions

hay còn được gọi là RegEx là một chuỗi văn bản đặc biệt giúp tìm các mẫu trong dữ liệu. Một RegEx có thể được sử dụng để kiểm tra xem một số mẫu có tồn tại trong một biểu thức chính quy không. 
## The re Module
`import re`

### Functions re trong module

Để tìm một mẫu, sủ dụng các bộ ký tự re khác nhau cho phép tìm kiếm một kết quả phú hợp trong chuỗi

* re.match() : Chỉ tìm kiếm ở dòng đầu tiên của chuỗi và trả về các đối tượng phù hợp nếu được tìm thấy, các đối tượng khác không trả về.
* re.seach(): trả về một đối tượng khớp nếu có một đối tượng ở bất kỳ đâu trong chuỗi, kể cả các chuỗi nhiều dòng.
* re.findall: Trả về danh sách tất cả các kết quả phù hợp
* re.split: lấy một chuỗi, chia nó tại các điểm khớp, trả về một danh sách.
* re.sub: Thay thế một hoặc nhiều kết quả phù hợp trong một chuỗi.

## match
```
# syntac
re.match(substring, string, re.I)
#substring là một chuỗi hoặc một mẫu, string là văn bản mà chúng ta tìm kiếm một mẫu,re.i là bỏ qua.
```

## Search
```
# syntax
re.match(substring, string, re.I)
```

## Tìm kiếm tất cả các kết quả phù hợp bằng cách sử dụng findall

Replacing a Substring