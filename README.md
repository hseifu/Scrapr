# Scrapr
Scrapr is a program to get information about preferred topics from the internet in a desired format.

## Transcript
Retrieves university transcript from Campusnet, then notifies the user of any changes.

#### Remarks
 Had to use **`selenium`** because I couldn't perform the login using **`requests`** :
 the log in *`form`*'s `action` is set to `/some/file.dll` and not a `url`. 
