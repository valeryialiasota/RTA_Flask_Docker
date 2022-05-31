FROM python:alpine3.7
COPY . /flaskProject
WORKDIR /flaskProject
RUN pip install -r requirements.txt
COPY model_rta.pkl /flaskProject
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]