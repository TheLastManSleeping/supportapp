FROM python:3.7
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1
WORKDIR /home/oem/task/supportapp
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pip install cached-property
RUN pipenv install --system --deploy
COPY . /home/oem/task/supportapp
RUN chmod +x /home/oem/task/supportapp/entrypoint.sh
CMD ["/home/oem/task/supportapp/entrypoint.sh"]


