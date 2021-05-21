# Check Port and status web
## Check Port 
* Sử dụng API của telegram để check port đang mở
* Check staus website


### Chuẩn bị
* 1 bot Telegram
* 1 server linux : CentOS-7

## Thực hiện cài đặt
Thực hiện cài đặt Python3 và các gói cần thiết:
```
yum install -y python3

<!-- yum groupinstall "Development Tools" -y
yum install python3-devel -y
yum install python3 -y
yum install python3-pip -y
pip3 install virtualenv
yum install -y git curl  -->
```

### Thực hiện tải source code
```
cd /opt
git clone https://github.com/huydv398/python-tutorial.git
cd python-tutorial/py
```

Thay Token của bạn vào:
`sed -i 's/<your_API>/TOKEN = "YOUR_TOKEN"/' /opt/python-tutorial/py/config.py`
Chỉnh sửa file config.py:
```
sed -i 's/<your_API>/TOKEN = "1899040673:AAGAa2H1hAfNJx0YzixrvVESBeK6b5voe1w"/' /opt/python-tutorial/py/config.py
```

* Lấy API Shodan: Truy cập [shodan.io](https://account.shodan.io/login) để lấy API Key của Shodan.
    * Thay API bạn vừa lấy vào câu lệnh sau:
    ```
    sed -i 's/<your_API_Shodan>/"API Shodan"/' /opt/python-tutorial/py/config.py
    ```
    * Nếu không có bạn có thể sử dụng API shodan sau: 1iyY8S7elAIY9P4i9ISZKUOV4DSBdQpl 
### Thực hiện tạo env
* Tạo môi trường ảo
```
python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
deactivate
```

* Cài đặt requirement. Tên các module được sử dụng trong python3.
`pip3 install -r requirements.txt`
### Tạo file service để chương trình chạy như một dịch vụ.
* Tạo file service nội dung sau, thực hiện câu lệnh:
```
echo """
[Unit]
Description= Check info IP or Domain
After=network.target

[Service]
PermissionsStartOnly=True
User=root
Group=root
ExecStart=/opt/python-tutorial/py/python3-virtualenv/bin/python3 /opt/python-tutorial/py/code.py --serve-in-foreground

[Install]
WantedBy=multi-user.target """ > /etc/systemd/system/ipinfo.service
```