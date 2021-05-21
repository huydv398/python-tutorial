# Check Port and status web
## Check Port 
* Sử dụng API của telegram để check port đang mở
* Check staus website


### Chuẩn bị
* 1 bot Telegram
* 1 server linux : CentOS-7

## Thực hiện cài đặt
Kiểm tra xem đã có version python3 trong máy chưa
```
python3 --version
```

Thực hiện cài đặt Python3 và các gói cần thiết:
```
yum groupinstall "Development Tools" -y
yum install python3-devel -y
yum install python3 -y
yum install python3-pip -y
pip3 install virtualenv
yum install -y git curl 
```