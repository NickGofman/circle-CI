FROM python:3.9.2-alpine

# upgrade pip
RUN pip install --upgrade pip
ENV VIRTUAL_ENV=/home/app/venv

# get curl for healthchecks

# permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app

WORKDIR /home/app
USER nonroot



# copy all the files to the container
COPY --chown=nonroot:nonroot . .
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py

RUN pip install gunicorn && pip install -r requirements.txt


CMD gunicorn --bind 0.0.0.0:9090 wsgi:app

