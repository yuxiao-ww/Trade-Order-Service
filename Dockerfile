# 选择 Python 3.9 作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /backend

# 复制项目文件
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行 FastAPI
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
