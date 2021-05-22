# Python PIP - Python Package Manager
## PIP là gì
PIP  là viết tắt của Preferred installer program- chương trình cài đặt ưu tiên. Sử dụng pip để cài đặt các gói python khác nhau. Package là một module python có thể chứa một hoặc nhiều module hoặc các package khác. một module hoặc các module mà có thể cài đặt vào ứng dụng là một package. Trong lập trình, chúng ta phải viết mọi chương trình tiện ích, thay vào đó chúng ta cài đặt các package và import chúng vào ứng dụng của mình.

Cài đặt pip
```
yum install -y python3
```

## Cài đặt các package bằng pip
Cài đặt numpy được gọi là numeric python. Nó là một trong những gói phổ biến nhất trong cộng đồng machine learning và khoa học dữ liệu- data science community

* numpy là các gói cơ bản cho tính toán khoa học- scientific computing với python. Nó chứa trong số nhưng thứ khác:
    * 
* Pandas là một thư viện mã nguồn mở, được cấp phép BSD cung cấp các cấu trúc dữ liệu hiệu suất cao, dễ sử dụng và các công cụ phân tích dữ liệu cho ngôn ngữ lập trình Python. Hãy cài đặt người anh lớn của numpy, Pandas

* Mở trang web.
```
import webbrowser


url_lists = [
    'http://onedata.vn',
    'https://fb.com/huyts9',
    'https://kb.onedata.vn',
]

for url in url_lists:
    webbrowser.open_new_tab(url) # chạy lệnh này desktop sẽ mở các trang web
```
## Gỡ cài đặt Packages
```
pip uninstall packagename
```

## Danh sách các gói
Để xem các gói đã cài đặt trên máy của chúng tôi. Chúng ta có thể sử dụng pip theo sau là danh sách.
```
pip list
```

## Đọc từ URL
Bây giờ bạn đã quen với cách đọc ghi trên tệp nằm trên máy local. Chúng tôi muốn đọc từ một trang web sử dụng url hoặc 1 API. Nó là một phương tiện để trao đổi dữ liệu có cấu trúc giữa các máy chủ chủ yếu dưới dạng dữ liệu json. Để mở một kết nối mạng, chúng ta cần một gói được gọi là `requests` nó cho phép mở một kết nối mạng và thực hiện hoạt động CRUD(create, read, update and delete). Trong phần này, chúng tôi sẽ chỉ đề cập đến việc đọc một phần của CRUD.install :
```
 pip3 install requests   
```

Chúng ta sẽ thấy các phương thức `get`, `status_code`, `headers`, `text` và `json` trong module requests:
* get(): để mở mạng và tìm nạp dữ liệu từ url - nó trả về một đối tượng phản hồi
* status_code: Nếu chúng tôi tìm nạp dữ liệu, chúng tôi có thể kiểm tra trạng thái của hoạt động (thành công, lỗi, v.v.)
* headers: To check the header types
* text: để trích xuất văn bản từ đối tượng phản hồi đã tìm nạp
* json: để trích xuất dữ liệu json Chúng ta hãy đọc một tệp txt dạng trang web này,

Hãy đọc từ một api. API-Application Program Interface: là viết tắt của Giao diện chương trình ứng dụng. Nó là một phương tiện để trao đổi dữ liệu cấu trúc giữa các máy chủ chủ yếu là dữ liệu json.
```
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' #nguồn dữ liệu

response = requests.get(url) # Mở và tìm nạp dữ liệu
print(response)
print(response.status_code) # status code
print(response.headers)     # headers information
print(response.text) 
```

## Creating a Package

Một lượng lớn các tệp trong các thư mục và thư mục con khác nhau dựa trên một số tiêu chí để chúng tôi có thể tìm và quản lý chúng một cách dễ dàng. Như bạn đã biết, Một module có thể chứa nhiều đối tượng, chẳng hạn như class, function, v.v. Một package có thể chứa một hoặc nhiều module có liên quan. Một package thực sự là một thư mục chứa một hoặc nhiều tệp module. hãy tạo một gói có tên là mypack, theo các bước sau:
```
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

Như các bạn thấy thư mục có chưa một tệp đặc biệt có tên init.py - tệp này lưu trữ nội dung của gói. Nếu đặt init.py trong thư mục, py bắt đầu nhận ra là một package. init.pt hiển thị các tài nguyên được chỉ định từ các module của nó để được nhập vào các tệp python khác. Tệp init.py trống làm cho tất cả các chức năng khả dụng khi một gói được nhập. 
## Thông tin thêm về các gói
* Database 
    * SQLAIchemy hoặc SQLOject - Hướng đối tượng truy cập vào một số hệ thống csdl
        pip install SQLAIchemy
* Web Development
    * Django - Framework web cấp cao
        * pip install diango
    * Flask -microframework cho Python dựa trên Werkzeug, Jinja 2
        * pip install flask
* Phân tích cú pháp HTML 
    * Beautiful soup - Trình phân tích cú pháp HTML/XML được thiết kế cho các dự án quay vòng nhanh như quét màn hình, sẽ được chấp nhận đánh dấu không hợp lệ.
        * pip install beautifulsoup4
    * PyQuery - Thực hiện jQuery bằng Python; Nhanh hơn beautifulsoup
* XML Processing
    * ElementTree -The Element type là một đối tượng chứa đơn giản nhưng linh hoạt, được thiết kế để lưu trữ các cấu trúc dữ liệu phân cấp, chẳng hạn như các tập tin XML đã đơn giản hóa, trong bộ nhớ. --Lưu ý: Python 2.5 trở lên có ElementTree trong Thư viện chuẩn
* GUI
    * PyQt - Ràng buộc cho framework Qt đa nền tảng.
    * TkInter - Bộ công cụ giao diện người dùng Python truyền thống.
* Data Analysis, Data Science and Machine learning
    * Numpy: Numpy (numeric python) được biết đến là một trong những thư viện machine learning phổ biến nhất trong Python.
    * Pandas: là một thư viện machine learning bằng Python cung cấp các cấu trúc dữ liệu cấp cao và nhiều công cụ để phân tích.
    * SciPy: SciPy là một thư viện machine learning dành cho các nhà phát triển ứng dụng và kỹ sư. Thư viện SciPy chứa các mô-đun để tối ưu hóa, đại số tuyến tính, tích hợp, xử lý hình ảnh và thống kê.
    * Scikit-Learn: Đó là NumPy và SciPy. Nó được coi là một trong những thư viện tốt nhất để làm việc với dữ liệu phức tạp.
    * TensorFlow: là một thư viện machine learning do Google xây dựng.
    * Keras: được coi là một trong những thư viện học máy thú vị nhất trong Python. Nó cung cấp một cơ chế dễ dàng hơn để thể hiện mạng neural. Keras cũng cung cấp một số tiện ích tốt nhất để biên dịch mô hình, xử lý tập dữ liệu, trực quan hóa đồ thị và hơn thế nữa
* Network:
    * request: là một gói mà chúng tôi có thể sử dụng để gửi yêu cầu đến máy chủ (GET, POST, DELETE, PUT)

### Đọc dữ liệu
