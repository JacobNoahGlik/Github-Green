# Github-Green
Never have grey squares on your github again. This will make sure you have made a commit (or make one for you if one does not exist) to github every day.

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
* Have random logical code added in case we run out of user's code
  * Figure this out later, for now generate garbage and upload it to github
* Keep track of streaks and email the user once a week with an update
  * See my [github emailer.py](https://github.com/JacobNoahGlik/Emailer) for reference
