FROM tiangolo/uwsgi-nginx-flask:latest
COPY main.py  /app
COPY test.sh  /app

CMD ["/app/main.py"]
ENTRYPOINT ["python"]