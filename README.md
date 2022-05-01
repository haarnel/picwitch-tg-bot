# About

Pet project. Bot for basic image manipulations right inside Telegram using aiogram + my full async web server for [pilimg-server](https://github.com/haarnel/pilimg-server). It works pretty well, but requires a lot of validations + throttling settings before upload it to production server.

Demo: [Watch](https://vimeo.com/582540139)

## Installation  (Docker)

```shell
git clone https://github.com/haarnel/picwitch-tg-bot
cd picwitch-tg-bot
# Rename .env_dist to .env and also specify your BOT_TOKEN inside .env file.
mv .env_dist .env
docker-compose up --build
```
