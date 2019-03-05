# ss和ssr链接解析

## ss解析
在 Base64 编码之前，ss链接的格式是这样的：

	ss://method:password@server:port

那么如何解码? 在解码前，如果字符串中有包含 – 和 _ 的字符，要先分别替换为 + 和 / , 然后再通过 base64_decode 解码就行了。

## SSR解析

在 Base64 编码之前，ssr 链接的格式是这样的：

	ssr://server:port:protocol:method:obfs:password_base64/?params_base64

上面的链接的不同之处在于 password_base64 和 params_base64 ，顾名思义，password_base64 就是密码被 base64编码后的字符串，而 params_base64 则是协议参数、混淆参数、备注及Group对应的参数值被 base64编码 后拼接而成的字符串。

即 params_base64为这些字段的拼接：

	obfsparam=obfsparam_base64&protoparam=protoparam_base64&remarks=remarks_base64&group=group_base64

## 实例

那么，假设现在有这样一个 ssr 链接：

	ssr://NDUuMzIuMTMxLjExMTo4OTg5Om9yaWdpbjphZXMtMjU2LWNmYjpwbGFpbjpiM0JsYm5ObGMyRnRaUS8_cmVtYXJrcz1VMU5TVkU5UFRGOU9iMlJsT3VlLWp1V2J2U0RsaXFEbGlLbm5wb19sc0x6a3Vwcmx0NTdsbktQa3ZaWGxvWjVEYUc5dmNHSG1sYkRtamE3a3VLM2x2NE0mZ3JvdXA9VjFkWExsTlRVbFJQVDB3dVEwOU4

将"ssr://"去掉，然后如果字符串中有包含 – 和 _ 的字符，要先分别替换为 + 和 / 


解码后的字符串如下：

	45.32.131.111:8989:origin:aes-256-cfb:plain:b3BlbnNlc2FtZQ/?remarks=U1NSVE9PTF9Ob2RlOue-juWbvSDliqDliKnnpo_lsLzkuprlt57lnKPkvZXloZ5DaG9vcGHmlbDmja7kuK3lv4M&group=V1dXLlNTUlRPT0wuQ09N

然后再把password_base64/?params_base64这些字符串提取出来:

password_base64是
	
	b3BlbnNlc2FtZQ

params_base64是

	remarks=U1NSVE9PTF9Ob2RlOue-juWbvSDliqDliKnnpo_lsLzkuprlt57lnKPkvZXloZ5DaG9vcGHmlbDmja7kuK3lv4M&group=V1dXLlNTUlRPT0wuQ09N

然后再次解码即可.

## code

#### 将SSR链接放入SSR.txt内，使用控制台$python main.py即可. 如果在IDE内执行不会输出到result.txt内

### main.py是程序主入口

### SSR_parse.py是对SSR进行解析

### PingIP.py是看IP是否能ping通

### LocateIP.py是用来定位IP

### SSR.txt内保存的是SSR链接

### result.txt是运行结果
