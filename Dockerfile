FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY first-app.py .
ENV PORT 5000
CMD ["python", "first-app.py"]
