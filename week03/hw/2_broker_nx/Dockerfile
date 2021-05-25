FROM alpine:latest 
RUN apk update && apk upgrade
RUN apk add mosquitto

EXPOSE 1883

CMD ["mosquitto"]
