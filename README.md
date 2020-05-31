# Discord Minecraft Server Status

Bot will display the status of a minecraft server as it's status and activity

## Build And Run

### Build docker image

```
docker build .
```

### Set env variables

Open .env.example and set the variables to your discord token and server address

```
DISCORD_TOKEN
```

Token for your bot from https://discord.com/developers/applications

```
MC_SERVER_ADDRESS
```

Address of the minecraft server

Rename `.env.example` to `.env`


### Run docker image

```
docker run -d --env-file .env [image_id]
```