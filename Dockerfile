FROM golang:1.20.2-windowsservercore-ltsc2022


WORKDIR /app

COPY cmd/SteamCMDWrapper ./
COPY pkg ./

COPY go.mod ./
COPY go.sum ./
RUN go mod download

RUN go build -o /SteamCMDWrapper

CMD [ "/cmd/SteamCMDWrapper/SteamCMDWrapper" ]
