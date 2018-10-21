FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# ENV TZ=America/Los_Angeles
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sudo echo "America/Los_Angeles" > /etc/timezone
RUN sudo dpkg-reconfigure -f noninteractive tzdata

ENTRYPOINT ["python"]
CMD ["app.py"]
