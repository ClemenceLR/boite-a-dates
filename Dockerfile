FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install waitress && pip install -r requirements.txt

ENV FLASK_APP=boite_a_dates \
    FLASK_ENV=production \
    FLASK_DEBUG=on \
    CORS_URL=http://localhost:5000

COPY . .

CMD [ "waitress-serve", "--port=5000", "--call", "boite_a_dates:create_app"]