FROM python:3.8-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y tzdata
ENV TZ Asia/Kolkata
RUN chmod +x BotCronScript.sh
#RUN ./BotCronScript.sh
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
ENTRYPOINT ./BotCronScript.sh 

