# NGINX+uWSGI+bottleのサンプル
## 必要な準備
### CentOS 7の場合
- nginxのインストール
`/etc/yum.repo.d/nginx.repo`を追加  
```
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```
- yumを実行  
`yum install -y nginx`

- python3のインストール  
CentOSではEPLE repositroyの追加が必要  
`yum install epel-release`  
python3のインストール  
`yum install python3 python3-devel python3-pip`

- bottle frameworkとuWSGIのインストール  
`pip3 install bottle uwsgi`

## nginxとuwsgiとbottleの関係 
- nginx 
HTTP REQUESTをWSGIのフォーマットで指定されたsocketに流し込みます.  
また、socketより返答を受け取ります.  
- uWSGI(Python Librayおよびサーバ)
socketより流し込まれてたHTTP Requestを指定されたpythonに流し込みます
また、socketより返答を受け取ります. 
- bottle (Python Libray)
WSGIでHTTPを処理できるpythonのweb frameworkです.
- block図

```
                +-------+     +----------------------------------------------------------------+
                |       |     | +-------+                +---------------------------------+   |
http access <-> | nginx |  -  | |socket |  uWSGI Server  | call app using bottle framework |   |
                |       |     | +-------+                +---------------------------------+   |
                +-------+     +----------------------------------------------------------------+
```
- 要点
 nginxとapplicationがuWSGI Serverを介して動いているので開発/デプロイが分離しやすい.
