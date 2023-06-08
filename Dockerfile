FROM python:3.9.6-buster
WORKDIR /app
#RUN pip install psutil
COPY read_procfs.py .
COPY check.sh .
#CMD ["python", "./read_procfs.py"]
CMD ["bash", "./check.sh"]
