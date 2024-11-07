FROM python:3.10-slim
ARG API_KEY
ENV API_KEY=${API_KEY}
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]