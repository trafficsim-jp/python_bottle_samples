# Nginx+uWSGI+bottleの動かし方.

## Nginx側の設定
### uWSGIを通じてhtmlを出力するvirtual hostを設定
rootにて設定を行います.  
`/etc/nginx/conf.d/`以下に.confファイルを作成します.  
```
server {
    listen       8080;
    server_name  localhost;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/uwsgi_8080.sock;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```
- 8080 portに来たHTMLアクセスを受けます
- http://xxx.xxx.xxx.xxx:8080/ は`/tmp/uwsgi_8080.sock`のunix domain socketを通じてbottleに流れます.

```
systemctl restart nginx
```
にて再起動します.

## uwsgi側の設定
### uwsgiのアプリケーションの起動
uwsgi.iniを記述し、以下のようなコマンドを起動します. rootにならなくても大丈夫です.
```
uwsgi --ini uwsgi.ini
```
### uwsgi.iniの内容
```
[uwsgi]
socket       = /tmp/uwsgi_8080.sock
pidfile      = ./uwsgi.pid
daemonize    = ./uwsgi.log
chdir        = ./
master       = 1
file         = hello.py
chmod-socket = 666
uid          = kaz
gid          = "domain users"
```
- nginxからの入力流し込み口として`/tmp/uwsgi_8080.sock`
- ./uwsgi.pidにpidを記録します
- ./uwsgi.logにlogを出力します
- hello.pyを読み込んで起動します
- socketのアクセス権限は666です.
- 起動したuwsgiアプリケーションのuid,gidです.


