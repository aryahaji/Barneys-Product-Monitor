FROM python:3-onbuild
ADD monitor.py /
CMD ["python", "./monitor.py"]