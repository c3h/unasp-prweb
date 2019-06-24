FROM python:3
LABEL maintainer Daniel Joveliano "daniel.joveliano@outlook.com"

COPY . /app
WORKDIR /app
RUN pip install -r requirements
CMD ["/bin/bash", "-c", "python app-back.py"]
