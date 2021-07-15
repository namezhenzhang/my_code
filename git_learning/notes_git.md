# GIT

---------------------------------
[TOC]
------------------------------

## 版本控制

- 开发和维护

- 版本更新（可以回退

- 多人编译同一个文件，每个人有不同的版本，不光能管理文件，还能管理文件内容

- 快照？

- 版本控制工具：

  - 协同修改、数据备份、版本管理、权限控制、历史记录、分支管理

- 版本控制简介

  1. 集中式：svn

		服务器宕机，历史数据全部消失（只留有当前版本

  2. 分布式：区块链

		所有版本在本地都有存储

- Linus: talk is cheap, show me the code

- git网址：git-scn.com

- 分支、快照

## git介绍

- 本地库、暂存区、工作区
- 工作区 -> git add -> 暂存区 -> git commit -> 本地库
- GitHub: git 的代码托管中心
- 本地库-》push-》远程库-》clone-》本地库
- fork变成自己的库-》pull request-》审核-》merge-》被fork的库

## git命令行操作

1. 本地库初始化

    ```git
    git init
    ```

2. 设置签名
	1. 形式
	- 用户名 
		```git
		git config --global user.name "你的用户名"
		```
		
	- Email 地址
	
		```git
		git config --global user.email "你的邮箱"
		```
	2. 区分不同开发人员
	3. 与登录远程库账号密码没有关系
	4. 命令
		- 项目&仓库级别：仅在当前本地库范围内生效
		  - git config user.name/email
		- 系统用户级别：登陆当前操作系统的用户范围
		- git config --global user.name/email
	
3. 状态查看
	
	```git
	git status
	```
	
4. 添加操作
	```git
	git add <filename>
	```
	```git
	git add --all
	```
	这个命令还会把删除的文件也提交进去
	```git
	git add .
	```
	不会记录删除操作

5. 提交操作
	```git
	git commit -m "commit message" <filename>
	```
	重写上一次的提交信息（发现注释写错了后可以修改）
	```
	git commit --amend
	```

  	新建文件需要add，之后只需commit

6. 版本记录

     git log [--pretty=oneline, ]

     git reflog

    -  多屏显示控制方式
    	1. 空格向下翻页
    	2. b向上翻页
    	3. q退出

7. 版本控制

  	1. 基于索引值操作
		```git
		git reset --hard <索引值>
		```
  	2. 使用^符号: 只能后退
		```git
		git reset -hard HEAD^
		```
	3. 使用~符号,: 只能后退
	```git
	git reset --hard HEAD~n
	```
  
	4. reset 3个命令参数对比

     	1. --soft
			- 仅在本地库移动HEAD指针

     	2. --mixed
			- 在本地库移动指针
			- 重置暂存区

     	3. --hard
			- 在本地库移动指针
			- 重置暂存区
			- 重置工作区 

	5. 找回删除文件
		```git
		get reset --hard [指针位置]
		```
  	6. 比较文件差异
		```git
    	git diff [文件名]
		```
    	- 将工作区中的文件和暂存区进行比较
		```
		git diff [本地库中历史版本] [文件名]
		```
     	- 不带文件名比较多个文件
		```git
    	git diff
		```

8. 分支操作

    - 创建分支
		```
      	git branch [分支名]
		```
		```git
		git checkout -b <branchname>
		```
    - 查看分支
		```
    	git branch -v
		```
    - 切换分支
		```
		git checkout [分支名]
		```
	- 合并分支
		```
		git merge
		```
	- 解决冲突
		- 人工修改
	- 修改分支名称
		```
		git branch -m [分支名] [新的分支名]
		```
	- 保存当前工作切换分支
		```
		git stash
		```
		查看当前存储了多少工作状态
		```
		git stash list
		```
		切换回刚刚的分支
		```
		git stash pop
		```
		> git stash pop会将list保存的列表也给删除掉
		> git stash apply 不会删除列表里的内容会默认恢复第一个
		> 如果想恢复指定内容可以使用git stash apply list名称
		> git stash drop list名称可以移除指定list
		> git stash clear 移除所有lsit
		> git stash show 查看栈中最新保存的stash和当前目录的差异。
		> stash是以栈的方式保存的，先进后出。
		> 准确来说，这个命令的作用就是为了解决git不提交代码不能切换分支的问题。
	- 将别的分支修改转移到自己的分支
		```git
		git cherry-pick
		```

	- 其他
		- 如果你在任何分支下创建文件，没有提交到仓库，那么它在所有仓库都是可见的
	

git branch -m 分支名 新的分支名
9. 缓存区
	- 这里存放了你使用git add命令提交的文件描述信息，它位于.git目录下的index文件中

1. git基本组成框架
	> Workspace：开发者工作区
	> Index / Stage：暂存区/缓存区
	> Repository：仓库区（或本地仓库）
	> Remote：远程仓库

10. 将文件撤销回到最近一次修改的状态
	```git
	git checkout -- <filename>
	```
11. 查看单个文件可回滚版本
	```git
	git log filename
	```
	之后回滚
	```
	git reset <hash> <filename>
	```
12. 删除文件
	```
	git rm
	```
	将删除提交到缓存区(文件是否还存在?)
## git基本原理
1. 哈希
	1. 只能加密,不能解密
	2. 长度固定
	3. 小修改大变化
	4. 相同数据加密结果相同

## 创建远程库
1. 生成ssh密钥
	```
	ssh-keygen
	```
1. 添加成员
	- 找到你要开放的仓库，选择Manage access然后使用invite a cikkaborator添加成员就可以了。
1. 远程关联
	```git
	git remote add https://github.com/namezhenzhang/huashan.git
	```
	```git
	git remote add origin https://github.com/namezhenzhang/huashan.git
	```
	(不知道哪个对?)
2. git clone <url>

3. 推送到远程
	```
	git push <url> <branch>
	```
	```
	git push -u origin master
	```
	>-u：将本地仓库分支与远程仓库分支一起合并，就是说将master的分支也提交上去，这样你就可以在远程仓库上看到你在本地仓库的master中创建了多少分支，不加这个参数只将当前的master与远程的合并，没有分支的历史记录，也不能切换分支
	(不知道哪个对?)
4. pull = fetch + merge
	git fetch <远程库地址别名> <远程分支名>