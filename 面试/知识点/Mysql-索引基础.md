+ 活用`Explain`
+ 查看索引类型 `show index from table_name`
+ 全文索引`ALTE table_name ADD FULLTEXT (colunm)` 创建全文索引
+ 回表查询：通过索引中记录的rowid访问表中的数据就叫回表。回表次数太多会严重影响SQL性能，如果回表次数太多，就不应该走索引扫描，应该直接走全表扫描。
	+ *EXPLAIN命令结果中的Using Index意味着不会回表，通过索引就可以获得主要的数据。Using Where则意味着需要回表取数据。*
	+ 回表数据最好不要超过30%
+ 索引原则：
	+ 适合索引的列是where字句中的列
	+ 使用短索引
	+ 不要过度索引，否则会降低写操作的性能，只保持需要的索引有利于查询即可
+ 查看索引是否被使用 `show status like handler_read`
	+ `Handler_read_rnd_next` 值也很大说明正在进行大量的表扫描，说明索引利用不理想
	+ like 前导模糊不能命中索引
	+ 数据类型隐式转换不能命中索引
	+ 复合索引需要满足*最左匹配原则* :指的是查询条件中是否包含最左列的字段，和sql语句中的顺序无关
	+ union、in、or都能命中索引，建议用in cpu or>in>union
		+ 使用or，如果有一个条件没有索引，那么就不会命中索引，因为其他条件要扫全表
	+ 负向查询不能命中索引 !=、<>、not in、not exists等
	+ 范围查询可以命中索引，between，>，<=等
	+ 被查询列要被所建的索引覆盖，避免回表
	+ 建立索引的列不可以有null
+ update频繁的字段不宜建立索引，因为会变更b+树
+ 区分度不大的不宜建立索引，不能有效过滤数据
+ 业务上有唯一性的索引必须要建立唯一索引，避免脏数据
+ 多表关联时保证关联字段有索引
+ 一些错误观念：
	+ 索引越多越好 ×
	+ 抵制唯一索引 ×
	+ 过早优化 