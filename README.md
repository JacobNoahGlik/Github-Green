# Github-Green
Never have grey squares on your github again. This will make sure you have made a commit (or make one for you if one does not exist) to github every day.

<br>

## Where
Testing will be done on a seprate account to reduce security risk. Found [here](https://github.com/TheOfficialAlmond/test_repo).

<br>

## How
This project will be completed outside of github and will be uploaded to github using the project itself as a PoC

<br>

## Issues:
* **SOLVED:** ~~While trying to securely store the github token I ran into an issue: I can't store the token as an unencrypted string in the code or in a file. So I encrypted the file, but now I need to store the encryption key. Great back to square one.~~
  * Possible solutions:
    * Save the encryption key to an environment variable on the device to at least segment the secrate token into sections
    * Create an endpoint to store the token and use asymmetric encryption to 1. confirm the id of the `github-green bot`, and 2. securely send over the token
    * Possible alternative solutions involve: python secrate storage methods
    * Possible alternative solutions involve: using timebased encryption and creating temp tokens to view the data
    * Possible alternative solutions involve: having the user input the encryption key manually (like a password)
* Solution: Use [secure secrete storage](https://github.com/JacobNoahGlik/Secure-Secrete-Storage-AWS/tree/main) to save / access the github api token

<br>

## Requirements:

* Be able to check if a user has made a comit today (will run at 11:50 PM)
  * More info found [here](https://stackoverflow.com/questions/46855484/checking-if-a-user-made-a-commit-to-github-using-api-on-a-given-day)
* Be able to create a new commit
  * More info found [here](https://stackoverflow.com/questions/7119452/git-commit-from-python)
* Be able to only run once a day (using a scheduler)
  * More info found [here](https://docs.python.org/3/library/sched.html)
* Be secure
  * Any credentials must be securly stored (or better not stored) 
* Have access to the users backlog of code to upload in chunks to keep github green
  * Be able to upload code to the bot
* Run the bot on aws
  * See my [run python code on aws forever](https://github.com/JacobNoahGlik/RunScriptOnAWS-Forever) on github

## For the future:

* Keep track of streaks and email the user once a week with an update
  * See my [github emailer.py](https://github.com/JacobNoahGlik/Emailer) for reference
* Add a website endpoint so a user can add their github credentials to the website and upload their code so that they don't have to run the code on their end.
