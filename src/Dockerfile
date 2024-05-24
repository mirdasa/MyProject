FROM python:3.11.9-slim
RUN pip3 install Flask-Login
RUN pip3 install Flask-SQLAlchemy
COPY . /opt/app
WORKDIR /opt/app
CMD [ "python", "./app.py" ]