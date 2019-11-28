# HOW-DO-I API
A web API wrapper over the amazing `howdoi` tool with support for Telegram bot
API


## Usage

```
docker build -t howdoi-api .
docker run -p 5000:5000 howdoi-api
```

```
curl localhost:5000?query=loop+in+golang
```

### Deployment to Zeit

```
now -e TELEGRAM_BOT_TOKEN=AAA
```

## Reference

* https://github.com/gleitz/howdoi
