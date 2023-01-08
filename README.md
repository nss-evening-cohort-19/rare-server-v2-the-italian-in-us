# Rare-Italian Server

## Project Overview
This full stack group project was completed over a 2-week sprint to plan, execute, and practice our command over the development of a server and database. The front-end portion is available [here](https://github.com/nss-evening-cohort-19/rare-client-v2-the-italian-in-us). The team decided to focus on the handling of logic and case conversions in the backend with the goal of clean API calls returning exactly what we needed to the front end. 

Tech Stack: Python with Django framework, SQLite, Postman, React with Next.js, React-Bootstrap.


## Running The Project Locally for endpoint testing
### Clone the repository
  * In this repository, locate and click the green `<> Code` button 
  * Insure the SSH option is selected and copy the clone string
  * Navigate to the directory of you choosing in your terminal 
  * Run the command: git clone <"clone string"> 

### Open the database
  * Press: SHIFT + CMD + P
  * Select: SQLite: Open Database
  * Select: db.sqlite3

### Installations and database setup
Run the bulleted commands from the command line to _Install dependencies_, _Migrate tables to database_, and _Load Data to Database_.
  * `pyenv install`

  * `python manage.py migrate`

  * `python manage.py loaddata datadump`

### Update the linter
  _.vscode/settings.json_
  *  replace code with:
  ``` 
  {
  "python.linting.pylintEnabled": true,
  "python.linting.enabled": true,
  "python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
    "--django-settings-module=rare.settings",
],
}
```

### Start the server
* run `python manage.py runserver` in the terminal.
You should see:
```
System check identified no issues (0 silenced)
January 06, 2023 - 16:03:25
Django version 4.1.3, using settings 'rare.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Postman
* Open Postman and create a new directory
* Select Add Request from the ellipsis of the new directory

### Suggested endpoints

* Select `GET` next to the request URL
* Paste bulleted endpoints into Request URL

##### Posts
* http://127.0.0.1:8000/posts

Get Posts return a list of all posts created. The team utilized the Django depth to also return data from those nodes represented by a foreign key on the post dictionary for ease of rendering on the front end.

##### User
* http://127.0.0.1:8000/users/1
* Select the `Authorization` tab
* Select `OAuth 2.0` in the `Type` dropdown
* Paste `e1YJhTEtk4UYrwkiSiHbjVveMcM2` into the `Access Token` field
* Send request

This call gets a single user and uses a HTTP_Authorization header hide the Google uid of the user from the browser.  Being associated with a profile for the user on the front end, the team used the Django ORM to return the related data of posts, followers, and subscribers. A custom property is also included that returns a Boolean if the requesting user has subscribed to the user in the get request.

##### Reactions
* http://127.0.0.1:8000/reactions?userId=2&postId=6

Reactions on a post is a many to many relationship in our application.  A post_reaction is created when a user reacts to a post. 2 custom properties ("clicked" and "count").  "count" is reffering to how many times a reaction has been clicked by any user for the post, and "clicked" refers to if the user has clicked that reaction for the post.

##### Create Post Reaction
* Select `POST` next to the request URL
* http://127.0.0.1:8000/postreactions
* Select the `Body` tab
* Select `Raw`
* Select `JSON` in the dropdown to the right of raw
* Paste the following into the text field
```
{
    "postId": 6,
    "reactionId": 8,
    "userId": 2
}
```
* Send the request

This call will create a new post_reaction node. We decided to explore handeling case separation between Python and JS on the server in this instance, allowing the front-end to send camelCase keys when creating. Send the GET reactions request again to see that the count for reaction id: 8 has updated and will now be clicked: False.


## Front-End Repository
Please follow the link [Here](https://github.com/nss-evening-cohort-19/rare-client-v2-the-italian-in-us) if you wish to see the Fron-End Pportion.
 
