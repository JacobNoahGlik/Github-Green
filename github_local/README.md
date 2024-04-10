# Github-Green
Never have grey squares on your github again. This will make sure you have made a commit (or make one for you if one does not exist) to github every day.

<br>

## Where
Testing will be done on a seprate account to reduce security risk. Found [here](https://github.com/TheOfficialAlmond/test_repo).

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
