FROM python:3.9-slim

WORKDIR /app
COPY ./py /app
RUN chmod +x main.py

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]