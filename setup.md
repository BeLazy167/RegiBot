# RegiBot

A discord registration bot that can be used to register the participants in a specific tournament or competition reducing the work load for the admin.

## Installation

Download this project 

```bash
git clone https://github.com/JayP09/discfactbot.git
```

## Installing Dependencies

```bash
pip install requirements.txt
```

## Setting up `config.py`

- ### Setting up discord API:
1.Go to [DISCORD DEV PAGE](https://discord.com/developers/applications) and create a bot of your choice, then:
2. to get a user id check this [Article](https://medium.com/@Seth./how-to-retrieve-message-user-server-and-channel-ids-on-discord-3d83bd0327d4): 
```python
self.TOKEN = 'YOUR DISCORD BOT PUBLIC KEY HERE'
self.OWNER_IDS = ['YOUR USER ID HERE']
```

- ### Setting up MONGO DB:
Go to [MONOGO-DB](https://www.mongodb.com/) and 
1. signup and create a cluster 
2. click on connect, then connect to the application
3. select python 3.6 and above 
4. get the link 

EXAMPLE:

![DB_LINK](https://i.gyazo.com/247a79c3eb7c8a68a9623c408ad85c38.png)

only get the string inside (" ")
5. Enter your username and password and then paste the link here
```python
self.db_link = "your Mongo database link here"
```
