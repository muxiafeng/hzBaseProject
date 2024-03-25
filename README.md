## 测试用的小项目，挂在云服务器上，供自动化测试调用或压测调用

### 配置信息
+ ip：117.50.117.15
+ 服务port：5000

### 数据库信息
+ 数据库port：3306
+ 账号：root
+ 密码：mysql123？

### 接口列表
+ daletou
  + 说明：返回最近一次的大乐透开奖信息
  + url：/daletou
  + method：GET
  + 请求示例：http://ip:5000/daletou
  + 返回示例：{"code":200,"message":"第23128期大乐透开奖时间：2023-11-08，开奖号码为：01 05 07 12 13 02 06"}
+ personinfo
  + 说明：返回一条个人信息，包含姓名、手机号、地址
  + url：/personinfo
  + method：GET
  + 请求示例：http://ip:5000/personinfo
  + 返回示例：{"code":200,"message":{"address":"711 Wright Pike Apt. 813\nGrimesborough, DC 33815","name":"Lisa Fry","phone":"953.682.0576x25655"}}
+ newperson
  + 说明：模拟添加一条个人信息，入参name、phone，name为字符串，不为空和纯符号，phone为数字
  + url：/newperson
  + method：GET
  + 请求示例：http://ip:5000/newperson?name=tom&phone=123123123
  + 返回示例：{"code":200,"message":{"address":"87252 Dan Burgs\nWest Andrewmouth, DE 92473","name":"tom","phone":"123123123"}}
+ error
  + 说明：返回错误信息和状态码401
  + url：/error
  + method：GET
  + 请求示例：http://ip:5000/error
  + 返回示例：{"error":"未授权访问"}
+ json
  + 说明：输入一个json，拼接键值对返回一个字符串
  + url：/daletou
  + method：POST
  + 请求示例：http://ip:5000/json
  + 参数示例：{"name":"com.pregnancy","bundle":"com.pregnancy","ver":"9.10.0"}
  + 返回示例：{"code":200,"message":"name:com.pregnancy bundle:com.pregnancy ver:9.10.0 "}
+ login
  + 说明：模拟登录并返回cookie
  + url：/login
  + method：POST
  + 请求示例：http://ip:5000/json
  + 参数示例：{"name":"com.pregnancy","bundle":"com.pregnancy","ver":"9.10.0"}
  + 返回示例：
### TODO
+ 数据库连接