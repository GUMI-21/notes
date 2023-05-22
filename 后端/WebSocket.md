+ 长连接实现方法
	+ 1.
		+ net包根据conn直接实现，传输的bytes实现io.write和op.read即可
		+ 一个用户一个连接
	+ 2.
		+ 使用gorilla/websocket 实现，复用http协议的握手过程，连接成功后在handler层实现websocket协议