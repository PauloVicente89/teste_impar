FROM python:3.11.4-slim-buster
LABEL mantainer="pauloviana089@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY project /project
COPY ./docker/dev/scripts /scripts

WORKDIR /project

EXPOSE 8000

RUN apt-get update \
  && apt-get install -y build-essential libpq-dev libmagic1 gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv \
  && /venv/bin/pip install --upgrade pip \
  && /venv/bin/pip install setuptools wheel --upgrade \
  && /venv/bin/pip install --no-cache-dir -r /project/requirements.txt \
  && adduser --disabled-password --no-create-home duser \
  && mkdir -p /data/web/static \
  && mkdir -p /data/web/media \
  && chown -R duser:duser /venv \
  && chown -R duser:duser /data/web/static \
  && chown -R duser:duser /data/web/media \
  && chmod -R 755 /data/web/static \
  && chmod -R 755 /data/web/media \
  && chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["start.sh"]