FROM python

COPY . /backend

WORKDIR /backend

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["backend/app.py"]

