FROM python:3.9.6-buster
WORKDIR /app
COPY read_procfs.py .
CMD ["python", "./read_procfs.py"]
