# FROM python:3.6

# WORKDIR /app

# RUN /usr/local/bin/python -m pip install --upgrade pip
FROM python:3.6.1-alpine
# update pip to minimize dependency errors
RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP main.py

CMD ["flask", "run", "--host", "0.0.0.0"]