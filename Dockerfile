FROM django:1.8.5-python2

RUN groupadd django && useradd --create-home --home-dir /home/django -g django django
WORKDIR /home/django

ADD foosball_scores/requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8000

USER django
CMD python manage.py runserver 0.0.0.0:8000

