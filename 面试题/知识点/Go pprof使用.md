+ 可以生成类似火焰图、堆栈图、内存分析图
+ runtime/pprof：采集程序 （非server)的数据进行分析
+ net/http/pprof：采集HTTP Server的运行时数据进行分析
+ 互斥锁分析、阻塞分析、内存分析、CPU分析
```go
package main

import (
    "log"
    "net/http"
    _ "net/http/pprof"
    "github.com/EDDYCJY/go-pprof-example/data"
)

func main() {
    go func() {
        for {
            log.Println(Add("https://github.com/EDDYCJY"))
        }
    }()

    http.ListenAndServe("0.0.0.0:6060", nil)
}

var datas []string

func Add(str string) string {
    data := []byte(str)
    sData := string(data)
    datas = append(datas, sData)

    return sData
}
```
`go tool pprof http://xxxxx:6060/debug/pprof/profile?second=60`\
执行这个命令后默认进入pprof的交互式命令模式
+ pprof可视化
	+ go tool pprof -http=:8080 cpu.prof
	+ cpu.prof是上面命令生成的
	+ go tool pprof cpu.prof
+ 火焰图
	+ `go get -u github.com/google/pprof`
	+ `pprof -http=:8080 cpu.prof`