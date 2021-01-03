# WebsiteBlocker

Repo for my Website Blocker app to prevent distraction from social media

The mechanism is simple: 

By importing the datetime built-in library of Python we can use its functions to compare the time in live and to check with conditions

If the time now is between the working hours, for example, 9 to 5, then the program edits the hosts file in your etc folder (If you are Ubuntu user, if not change the pathname to the one specified in Windows or Mac configuration) in such a way, that it adds the distracting website link address into it, and blocks the access to it the entire time

On the other hand, if time specified is off the range, then program deletes the link addresses from hosts file, and access for these websites is open 

If you have any suggestions on how to improve the program, please don't hesitate to contact me via Telegram, my nickname is on my profile :) 
