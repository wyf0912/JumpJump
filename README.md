# 跳一跳辅助程序<bl>
## 环境要求<br>
python3.5+opencv+adb工具
## 使用方法<br>
运行autojump.py文件。默认分辨率是1920*1080的手机。计划之后使用摄像头加机械臂。
## 注意事项<br>
图像识别利用30度角和漫水填充，消除了累计误差，基本可以做到一直跳不死。<br>
但跳的太准的bug还没有修复，不要连续跳中心太多次，成绩容易被ban。

# 机械外挂部分<br>
此部分是为了以后实现摄像头加机械臂，添加的功能。
## 屏幕提取<br>
此部分是为了实现从图像中找到手机屏幕，并将其利用透视变换提取出来。效果及原理如下图<br>
![image](https://raw.githubusercontent.com/wyf0912/PlayOwnGame-with-DQN/master/github_src/屏幕提取示意.png)

