FROM python:3.13-slim

WORKDIR /docs

COPY ./docs/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["sphinx-build", "-b", "html", ".", "_build/html"]
