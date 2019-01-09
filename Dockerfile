FROM python:3-onbuild
ADD monitor.py /
RUN pip install lxml
CMD ["python", "./monitor.py"]