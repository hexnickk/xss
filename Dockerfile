FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /app
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install
COPY . /app/

EXPOSE 8000

CMD pipenv run gunicorn xss.wsgi \
    -b 0.0.0.0
