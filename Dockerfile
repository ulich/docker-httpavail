FROM python:3.4-slim

RUN pip install requests==2.5.1 retrying==1.3.3

ADD httpavail.py /

ENTRYPOINT ["python3", "/httpavail.py"]
