# Calendar-utility

In this utility, I have integrated Python with MySQL. Each user will have their own account and can add/delete/update/view events of their calendar. The program also creates a csv file containing each user's calendar years data.

For each user, a new database is created in MySQL, and for each calendar year the user accesses, a new table gets created containing all the dates of that years in one column, and X event columns where X is the maximum number of events on any date of that year. Lastly, there is a unique table which contains the password of the user.

I am looking forward to change the overall design to make the program consume less memory and make it more efficient. I am also planning to expand this project and make  it global-based rather than local-based by implementing django framework.
