FROM python:3.10

WORKDIR /app

COPY . /app

ENV PYTHONPATH=/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn  # Add this line to install Gunicorn

CMD ["gunicorn", "-c", "gunicorn_conf.py", "app.main:app"]
