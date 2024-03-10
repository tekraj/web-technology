FROM python:3.10
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY  ./ .
CMD [ "python3", "./app.py" ]