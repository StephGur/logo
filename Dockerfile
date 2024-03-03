# Use the official Python image as the base image
FROM python:3.9
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "server.py"]
