#### Linux
`curl xxxx | python -m json.tool` 将curl的返回json进行格式化
`nslookup` 
+ 虚拟内存
```bash
sudo fallocate -l 20G /mnt/.swapfile # 创建 20G 空文件  
sudo mkswap /mnt/.swapfile    # 转换为交换分区文件  
sudo chmod 600 /mnt/.swapfile # 修改权限为 600  
sudo swapon /mnt/.swapfile    # 激活交换分区  
free -m # 查看当前内存使用情况(包括交换分区)

sudo swapoff /mnt/.swapfile  
rm -rf /mnt/.swapfile
```
#### git
`git checkout branch path` 覆盖分支文件
`git add remote origin git@xxxx` 添加远程分支
`git rm -r --cached path` 删除本地git文件缓存
#### mysql
`unix_timestamp("2023-07-10 0:00:00")` 时间转时间戳