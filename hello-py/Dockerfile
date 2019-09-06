FROM python:3.7

WORKDIR /app
ADD . /app/
RUN pip --disable-pip-version-check --no-cache-dir install poetry \
    && poetry config settings.virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
