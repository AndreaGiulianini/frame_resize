FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "./resize_images.py", "--input_folder", "/app/input", "--output_folder", "/app/output"]

