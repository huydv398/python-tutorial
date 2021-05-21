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

* Tạo một phiên bản của lớp TeleBot. Token được thay thể bằng chuổi Token của bạn.
```
import telebot

bot = telebot.TeleBot("TOKEN", parse_mode=None) # Bạn có thể đặt parse_mode theo mặc định. HTML hoặc MARKDOWN
```

Sau khai báo đó, chúng ta cần đăng ký một số cái gọi là  message handlers- trình xử lý thông báo. Các trình xử lý thông báo xác định các bộ lọc mà một thông báo phải vượt qua. Nếu một thông báo vượt qua bộ lọc, decorated function sẽ được gọi và thông báo đến sẽ được chuyển như một đối số.

Hãy xác định một trình xử lý thông báo xử lý các lệnh đến /startvà /help

```
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Chào mừng các bạn?")
```
Nếu có lệnh /start hoặc /help thì sẽ trả lại tele đoạn ký tự *Chào mừng các bạn?*

Một hàm decorated bởi một trình message handler có thể có tên tùy ý, tuy nhiên, nó phải chỉ có một tham số (the message).
```
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
```
Điều này lặp lại tất cả các tin nhắn văn bản đến người gửi. Nó sử dụng một hàm **lambda** để kiểm tra một thông báo. Nếu **lambda** trả về True, thông báo sẽ được xử lý bởi hàm decorated. Vì chúng ta muốn tất cả các thông báo được xử lý bởi hàm này, chúng ta chỉ cần trả về True.

Lưu ý: tất cả các trình xử lý đều được kiểm tra theo thứ tự mà chúng đã được khai báo

Bây giờ chúng ta có một bot cơ bản trả lời một thông báo tĩnh cho các lệnh "/ start" và "/ help" và lặp lại phần còn lại của các tin nhắn đã gửi. Để khởi động bot, hãy thêm phần sau vào tệp nguồn của chúng tôi:

```
bot.polling()
```

Cuối cùng có tệp như sau:
```
import telebot

Token_id ='Token của bạn'
bot = telebot.TeleBot(Token_id)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Chào mừng các bạn?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text) # Nếu không trùng command nào được khai báo phía trên Message sẽ gửi về những gì mà người dùng nhập

bot.polling()
```

## General API Documentation
Tất cả các loại được định nghĩa trong styles.py. Tất cả chúng đều hoàn toàn phù hợp với định nghĩa của Telegram API về các loại , ngoại trừ trường Thông báo from, được đổi tên thành from_user(vì fromlà mã thông báo dành riêng cho Python). Do đó, các thuộc tính như message_id có thể được truy cập trực tiếp với message.message_id. Lưu ý rằng đó message.chat có thể là một trường hợp của User hoặc GroupChat(xem Làm cách nào để phân biệt Người dùng và Trò chuyện nhóm trong message.chat? ).

Đối tượng Message cũng có một content_typethuộc tính xác định kiểu của Message. content_type có thể là một trong những chuỗi kí tự sau: text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message.

## Message handlers
Trình xử lý tin nhắn- Message handler là một hàm decorated bằng trình message_handler decorated của một phiên bản TeleBot. Trình xử lý tin nhắn bao gồm một hoặc nhiều bộ lọc. Mỗi bộ lọc trả về giá trị True cho một thông báo nhất định để trình xử lý thông báo đủ điều kiện xử lý thông báo đó. Trình xử lý thông báo được khai báo theo cách sau (miễn bot là một phiên bản của TeleBot):
```
@bot.message_handler(filters)
def function_name(message):
	bot.reply_to(message, "This is a message handler") 
```
function_name không bị ràng buộc với bất kỳ hạn chế nào. Bất kỳ tên chức năng nào đều được phép với trình xử lý tin nhắn. Hàm phải chấp nhận nhiều nhất một đối số, đây sẽ là thông báo mà hàm phải xử lý. filters là danh sách các đối số từ khóa. Một bộ lọc được khai báo trong các cách sau đây: name=argument. Một trình xử lý có thể có nhiều bộ lọc. TeleBot hỗ trợ các bộ lọc sau:(filters=??)

* content_types(list of strings): True nếu message.content_type nằm trong danh sách các chuỗi.
* regexp (một biểu thức chính quy dưới dạng một chuỗi): True nếu re.search(regexp_arg) returns True and message.content_type == 'text'
* commands(list of strings): True if message.content_type == 'text' and message.text bắt đầu bằng một lệnh nằm trong danh sách các chuỗi.
* func(lambda hoặc hàm tham chiếu): True if the lambda or function reference returns True