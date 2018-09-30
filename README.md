#Reddit MemeEconomy Scanner#

Required Modules:
  notify-run,
  webbrowser,
  time,  
  requests
  

Comes with two files for completing the desired task.
1) A number of classes for interpreting the Reddit API. This produces data of each post found in rising, top, new...etc sections as well as sorting the data under named keys in dictionaries.
2) The main function which uses (1) for retrieving information on the newest posts on www.reddit.com/r/memeeconomy any post which has more than 2 upvotes for each minute old it is, and is between 10-15 minutes old will be sent to the user's phone in the form of a notification and post link.

--Why?--
MemeEconomy on reddit has an investment function which users can comment on entertaining pictures "investing" artificial currency for a larger return. The return is based on how many upvotes the post receives in the following 4 hours, with lower vote investments returning (possibly) larger amounts with additional risk associated.

Generally the best investments are at a >2 upvotes per minute, and any post under 30 votes when invested in, will return up to 100% on the initial investment. Hence the 10-15minute age criteria
