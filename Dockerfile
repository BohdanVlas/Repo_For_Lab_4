FROM python:3
ADD Lab4.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 8080
CMD [ 'python', './Lab.4py']