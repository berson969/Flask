FROM python:3.10

RUN apt update && apt install -y curl

COPY requirements.txt .


RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./advs ./adv

WORKDIR /advs
EXPOSE 5000

RUN chmod +x /usr/src/adv/entrypoint.sh

ENTRYPOINT ["/home/adv/entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
