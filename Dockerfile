# 基于Python官方镜像
FROM python:3.8-slim
 
# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
 
# 创建工作目录
WORKDIR /app
 
# 复制当前目录下的文件到工作目录
COPY . /app
 
# 安装项目依赖
RUN pip install -r requirements.txt
 
# 暴露容器端口5000
EXPOSE 5000
 
# 运行Flask应用
CMD ["flask", "run"]