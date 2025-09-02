FROM python:3.12.11-bookworm

WORKDIR /app

COPY src .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x prestart.sh

ENTRYPOINT ["./prestart.sh"]
CMD ["python3", "main.py"]

