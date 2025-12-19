the storage will be a CSV 

do a menu that contain :
1-Add transaction

2-View transactions

3-Filter by month/category

4-Show monthly summary

5-Exit

after the excuation we back to return to menu

Add transaction:
data  to input :
date (YYYY-MM-DD)

type (income or expense)

category (food, rent, transport, etc.)

amount (positive number)

note (optional)

after we store the transacation in the csv


View transactions:

All entries

Filter by month (e.g., show transactions where date is in chosen month)

Filter by category

Decide the output layout: date | type | category | amount | note


Show monthly summary:

Total income for month

Total expenses for month

Net balance (income − expenses)

Top 3 expense categories by total spent



List common input errors and how your program will respond:

Invalid date format → ask again

Non-numeric amount → warn and re-prompt

Unknown menu choice → show menu again

Decide how to handle missing/corrupt data in CSV (ignore or warn).