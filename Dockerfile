FROM python:3.9-slim

WORKDIR /app

RUN 

COPY . .

EXPOSE 8000

CMD ["python", "tictactoe.py"]
