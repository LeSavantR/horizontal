FROM python:3.11-alpine3.17
# Propiedad Horizontal.

ENV PYTHONUNBUFFERED=1

RUN apk add gcc g++ cmake make mupdf-dev freetype-dev libpq-dev

RUN pip install --upgrade pip

WORKDIR /app

COPY ["requirements.txt", "."]

RUN pip install -r requirements.txt

COPY [".", "."]

RUN chmod +x run.sh

EXPOSE 8000

CMD [ "sh", "run.sh" ]