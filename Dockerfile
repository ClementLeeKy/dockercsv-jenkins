FROM python:3

WORKDIR /demo

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u" , "./test.py"]
