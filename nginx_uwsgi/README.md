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
