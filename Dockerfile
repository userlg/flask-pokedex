FROM python:3.11-rc-slim-bullseye

WORKDIR /src

COPY . /src/

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python","run.py"]

