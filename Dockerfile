FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

RUN unzip app/models/variables.zip -d  app/models/

RUN rm app/models/variables.zip

CMD ["python", "app/main.py"]
