# Mys_Goods_Rob 米游社商店兑换工具（云函数）  
## 使用说明  
* 上传代码包  
* 通过环境变量配置参数  
  * 根据`goods_list.py`所获取的信息填写所需商品的`goods_id`  
    * 会打包成`.exe`方便方便使用
  * 下文将详细说明`mys_cookies`,`goods_id`,`uid`,`address`,`server`,`biz`等参数的获取方法  
  * 通过配置`SCTkey`，可以使用Server酱的推送服务
* 测试能否正常运行  
* 配置定时触发器（cron表达式）  
* 部署完成，可以摸鱼了  

## 所需环境变量  
|  变量名  |  key  |  value  |  获取方式  |
|  ----  | ----  | ----  | ----  |
|  商品id  |  goods_id  |  ----  | ----  |
|  米游社cookies  |  mys_cookies  |  ----  | ----  |
|  UID  |  uid  |  ----  | ----  |
|  地址id  |  address  |  ----  | ----  |
|  服务器  |  server  |  ----  | ----  |
|  biz  |  biz  |  ----  | ----  |
|  Server酱  |  SCTkey  |  ----  | ----  |
