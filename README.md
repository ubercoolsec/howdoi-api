# HOW-DO-I API
A web API wrapper over the amazing `howdoi` tool


## Usage

```
docker build -t howdoi-api .
docker run -p 5000:5000 howdoi-api
```

```
curl localhost:5000?query=loop+in+golang
```

## Reference

* https://github.com/gleitz/howdoi
