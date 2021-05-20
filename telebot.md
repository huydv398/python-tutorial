# Telebot
Thư viện này cung cấp giao diện Python thuần túy cho telegram bot API. Nó tương thích với các phiên bnar Python 3.6 trở lên.

Ngoài việc kiểm tra API thuần túy, thư viện này có một số lớn cấp cao để làm việc phát triển bot dễ dàng và đơn giản. Các lớp này được chứa module con telegram.ext 

Việc cài đặt kết hợp cả python-telegram-bot và python-telegram-bot-raw sẽ dẫn đến các tác dụng phụ không mong muốn, vì vậy chỉ cài đặt một trong cả hai.

## Cài đặt
Bạn có thể cài đặt hoặc nâng cấp python-telegram-bot với:
```
pip install python-telegram-bot --upgrade
```
## Phụ thuộc vào tùy chọn
PTB có thể được cài đặt với các phụ thuộc tùy chọn:
* `pip install python-telegram-bot[passport]` Thư viện mật mã. Nếu bạn muốn sử dụng chác năng liên quan đến telegram pasport 
* `pip install python-telegram-bot[ujson]` Cài đặt thư viện ujson. Sau đó, nó sẽ được sử dụng để giải mã và mã hóa JSON, có thể tăng tốc độ so với thư viện JSON tiêu chuẩn.
* `pip install python-telegram-bot[socks] ` Cài đặt thư viện PySocks. Nếu bạn muoonslamf việc sau một máy chủ socks5

## Bắt đầu
Giới thiệu về API
### API bot telegram thuần túy
API_bot được hiển thị thông qua `telegram.Bot` class. Các phương thức này tương đương với snake_case của các phương thức được mô tả trong Telegram_Bot_API. Tất cả các class của API_Bot cũng có thể được tìm thấy trong module telegram, ví dụ  **Message** class có sẵn duối dạng **telegram.Massage**

Để tạo mã Access Token, bạn phải nói chuyện với BotFather và làm theo một vài bước đơn giản.

