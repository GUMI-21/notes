+ 框架的核心作用
	+ 路由：支持动态路由，将请求映射到函数中
	+ 模版：使用内置模板引擎提供模版渲染机制
	+ 工具集：对cookies，headers等处理机制
	+ 插件：中间件机制，可以安装到全局，也可以针对几个路由生效
+ Gin的代码总共是14K，测试代码9K
+ http接口
```go
// If ServeHTTP panics, the server (the caller of ServeHTTP) assumes  
// that the effect of the panic was isolated to the active request.  
// It recovers the panic, logs a stack trace to the server error log,  
// and either closes the network connection or sends an HTTP/2  
// RST_STREAM, depending on the HTTP protocol. To abort a handler so  
// the client sees an interrupted response but the server doesn't log  
// an error, panic with the value ErrAbortHandler.  
type Handler interface {  
   ServeHTTP(ResponseWriter, *Request)  
}

func ListenAndServe(address string,h Handle) error
```
h:只要传入任何实现了 _ServerHTTP_ 接口的实例，所有的HTTP请求，就都交给了该实例处理了。
+ 对Web服务来说，无非是根据请求`*http.Request`，构造响应`http.ResponseWriter`。
+ 