FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ARG API_KEY
ENV API_KEY=${API_KEY}
CMD ["python", "app.py"]