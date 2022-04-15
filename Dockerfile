FROM python:latest

WORKDIR /src

COPY . /src/

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python","run.py"]

