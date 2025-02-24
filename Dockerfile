FROM python:3.9

# work dir
WORKDIR /backend

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# run FastAPI
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
