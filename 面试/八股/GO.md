### 基础
#### map并发是否安全
只读是安全的，读写是不安全的
不行，因为map是引用类型，会发生数据竞争，共享资源遭到破坏。解决：读写锁、sync.map
#### map删除一个key内存会释放么
map的元素是引用类型时不会释放，只会释放引用子元素的内存，map设置为nil时内存会被回手
#### 两个chan同时有值时，select会随机选择一个可用通道做收发操作
### 进阶
#### select中只有一个已经关闭的case 会怎么样
会发生死锁，select会阻塞住，所以一定要设置default
#### 对一个已经关闭的channel进行读写会怎么样
读已经关闭的可以读到东西，如果buffer中还有未读可以读到元素，否则第二个bool值会是false。
写的话会发生panic。
#### 对未初始化的chan进行读写，会怎么样
读写都会发生死锁，阻塞程序
#### GO GC时会发生什么
go gc会使用三色标记法并发生stop the worl和使用读写屏障。
根据引用次数标记，白色内存空间为不可达
#### Gorutine 如何进行调度
gourtine的本质是写成。 go func()
是使用gmp模型的，goroutine+thread+processor   协程+调度器+线程
M代表内核级线程，goroutine跑在M之上。groutine有自己的栈内存和上下文用于调度，processor就是处理器，用来维护goroutine队列。Sched代表调度器，维护有存储M和G的队列以及调度器的一些状态信息。
#### waitGroup用法
wg.add(int)设置协程数量，在协程中调用wg.done()，在外部调用wg.wait()执行block
wg主要维护两个计数器， 一个请求技术 一个等待计数。
#### 什么叫原子操作
就是表现成一个不可分割的整体，要么都执行 要么都不执行。
#### Sync.Pool
频繁的分配、回收会给GC带来很大的负担，严重会引起CPU的毛刺，而sync.Pool可以暂时将不用的对象缓存起来。下次需要的时候直接使用，不再经过内存分配。
#### 查看gourinte的数量
GOMAXPROCS可以控制和查看总协程数量