FROM node:8.6.0

ADD ./app /app

WORKDIR /app

EXPOSE 3000

RUN yarn install
RUN yarn
CMD ["yarn", "start"]