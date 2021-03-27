# RegiBot
### Description
>
>A discord registration bot that can be used to register the participants in a specific tournament or competition reducing the work load for the admin.

---

### Get yourself a basic idea on how the Regibot works.
- #### Admin's End
  - As soon as the **server admin** adds Regibot to the server, the **bot itself** creates a text-channel named `events-schedule` which can only be seen by the **server owner** and **server admins**.
  - For Example, when the **server admins** or the **server owners** types the command `reg create Hackathon` where `reg` is the **prefix**, `create` is the command and `Hackathon` is the **event name** it will create a category named `Hackathon` which will contain different **text-channels** and **voice channel** related to the event which can be accessed by every member who wishes to participate.
- #### User's End 
    - Members will have to register themselves by typing the following command:
    `reg serverID, eventName, teamName, discordId, name, age, email`
    <!-- For Example:
    Leader's Info followed by teammates where teammates info will be continued after the leader's info separating with a ','
    `reg serverID, Hackathon, LaziX, discordId, Rutvik, 20, rut27jo@gmail.com` -->
    - On succesful registration the **team leader** will receive a **random passcode** which can be used to **update** the team members or their info with the help of **team name** and **passcode** to avoid any confusions for the **admin**.

---

####Libraries Used
- [Discord.py](https://discordpy.readthedocs.io/en/latest/api.html#)
- [pymongo](https://docs.mongodb.com/drivers/pymongo/)
