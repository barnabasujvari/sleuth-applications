FROM python:3.8
WORKDIR /container
RUN pip install poetry
COPY . /container
RUN poetry config virtualenvs.create false
RUN poetry install
CMD poetry run container
