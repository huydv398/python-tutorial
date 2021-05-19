# Lấy nội dung trang web
Internet chứa nhiều dữ liệu khổng lồ có thể được sử dụng cho các mục đích khác nhau. Để thu thập dữ liệu này, chúng ta cần biết cách thu thập dữ liệu từ một trang web.

Gỡ bỏ trang web là quá trình trích xuất và thu thập dữ liệu từ các trang web và lưu trữ trên máy cục bộ hoặc trong csdl.

Trong phần này, chúng ta sẽ sử dụng gói beautyfoulSoup4 và request để quét dữ liệu:
```
pip install requests
pip install beautifulsoup4
```

Để thu thập dữ liệu từ các trang web, cần có hiểu biết cơ bản về các thẻ HTML và css. Mục tiêu nội dung từ một trang web bằng cách sử dụng các class, tag, ids. Import các module request và BeautifulSoup 

```
import requests
from bs4 import BeautifulSoup
```

