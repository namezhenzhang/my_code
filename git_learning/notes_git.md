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

   1. 命令：git add
   2. git init

2. 设置签名
	1. 形式
		- 用户名
		- Email 地址
	2. 区分不同开发人员
	3. 与登录远程库账号密码没有关系
	4. 命令
		- 项目&仓库级别：仅在当前本地库范围内生效
		  - git config user.name/email
		- 系统用户级别：登陆当前操作系统的用户范围
		- git config --global user.name/email

3. 状态查看
	git status
	
4. 添加操作
	git add <filename>
	
5. 提交操作
	git commit -m "commit message" <filename>
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

     - git reset --hard [索引值]
  2. 使用^符号: 只能后退
	
	- git reset -hard HEAD^
  3. 使用~符号,: 只能后退
     
- git reset --hard HEAD~n
  
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
  
- get reset --hard [指针位置]
  
  6. 比较文件差异

     - git diff [文件名]
       - 将工作区中的文件和暂存区进行比较
- git diff [本地库中历史版本] [文件名]
     - 不带文件名比较多个文件

14. 分支操作

    - 创建分支
      - git branch [分支名]
    - 查看分支
      - git branch -v
    - 切换分支
		- git checkout [分支名]
	- 合并分支
		-  切换分支, git merge
	- 解决冲突
		- 人工修改

## git基本原理
1. 哈希
	1. 只能加密,不能解密
	2. 长度固定
	3. 小修改大变化
	4. 相同数据加密结果相同

## 创建远程库

1. git remote add <name> <url>
	```git
	git remote add https://github.com/namezhenzhang/huashan.git
	```
2. git clone <url>

3. git push <url> <branch>

4. pull = fetch + merge
	git fetch <远程库地址别名> <远程分支名>