# vnet
python httpserver to mock http api server before you have a real one

##using
1 start server by run python vnet.py
2 place you json file(ex:"animation") under webbase/gets/v3/app/android/phone/

then you can get http response from http://[your_host:your_port]/v3/app/android/phone/animation


很多情况下，服务器开发慢吞吞的，等不及啦，需要自己调试一下。怎么办？

##使用说明
1 启动脚本：python vnet.py
2 自己写个json文件放到目录webbase/gets/v3/app/android/phone/

这样你就能通过http://[your_host:your_port]/v3/app/android/phone/animation访问这个脚本啦

windcao@hotmail.com
https://github.com/caojianfeng/vnet