# Virtual Environment
* `virtualenv` là một công cụ được sử dụng để tạo ra các môi trường chạy Python cô lập ( hay các Virtual Environment ) .
* Mỗi môi trường sẽ có các thư mục cài đặt riêng và môi trường chạy riêng . Chúng không chia sẻ môi trường với nhau . <br> => Rất hữu ích cho các ứng dụng yêu cầu nhiều môi trường riêng biệt trên cùng một server .
* Yêu cầu trước cài đặt virtualenv :
    * Python3
    * PIP
## Cài đặt virtualenv
```
pip3 install virtualenv 
```
```
[root@onedata ~]# pip3 install virtualenv
WARNING: Running pip install with root privileges is generally not a good idea. Try `pip3 install --user` instead.
Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/80/59/f8815ff01ac7eff0f628c454f2d2b4cace19b70ccc9dcdbc61c3eb7f599d/virtualenv-20.4.6-py2.py3-none-any.whl (7.2MB)
    100% |████████████████████████████████| 7.2MB 122kB/s 
Collecting importlib-resources>=1.0; python_version < "3.7" (from virtualenv)
...
```
## Tạo vitual environment
* Sử dụng lệnh để tạo **virtual environment**
```

```