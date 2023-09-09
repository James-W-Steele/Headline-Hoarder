Headline Hoarder is an automatic news retrieval system meant to deliver news more quickly and more easily than before.
It automatically scans the words on various news sites against its list of target words/tickers.
It's meant to deliver company news very easily, but can be used for other things too.
In order to effectively use the program, you should know how to add/delete sites, add/delete hits, and change settings.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ADD/DELETE SITES:

In order to add sites you think would be useful or delete ones that have not been receptive, you would first need to open up the Sites.txt text file. 
The file should look something like this:

https://finance.yahoo.com/
https://finance.yahoo.com/calendar
https://www.cnbc.com/companies/
https://www.cnbc.com/business/
https://www.investopedia.com/company-news-4427705
https://www.usatoday.com/money/business/

It has URL's listed one per line. In order to add a website, like NBC news for business, you would simply paste the URL on the next line.
Make sure to not add any spaces before, after, or in the URL.
Make sure that there are no blank lines.
At the end of the process, the file should look like this:

https://finance.yahoo.com/
https://finance.yahoo.com/calendar
https://www.cnbc.com/companies/
https://www.cnbc.com/business/
https://www.investopedia.com/company-news-4427705
https://www.usatoday.com/money/business/
https://www.nbcnews.com/business

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ADD/DELETE HITS

A hit is a term that I use to describe the target words the site is looking for in website data. 
The process of adding a hit is very similar to that of adding a website, but with a few more restrictions
As with adding a website, there should not be any spaces, and there should be only one hit per line.
However, due to the process of separating the HTML to regular text, there is a list of unsupported characters.

Here are all of the characters that will be automatically removed from the search algorithm:

>
<
=
+
#
%
\
:
/
'
"
;
{
}
(
)
-
.

Given that all of these characters are relatively rare, they  only impede few things.
In order to correctly identify hits when they occurr, all capital letters in the site data are automatically lowercased, so if you enter in a 
hit with capital letters in it, the hit will simply never be found

Here is an example of how to add the ticker BRK-B:
You would remove the dash, lowercase all letters, and remove the last B.
BRK-B would be correctly entered as: brk
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
UNDERSTANDING SETTINGS

In the settings file, there are five different settings that you can change to alter the way the program handles hits.
I will go through the different settings and describe what each of them means.


STM:
STM stands for Short Term Memory. It's a variable that records the last registered hit. This variable prevents consecutive hits of the same name from being shared to the user.
This is meant to prevent the same headline from being shared twice, as many headlines will use the hit multiple times in the headline.
Example: Facebook shares soar as millions sign up for Facebook's new cloud share service!
Having STM activated would prevent this headline from being shared twice, as the program would detect facebook twice, but STM would prevent consecutive instances of facebook.

LTM:
As I'm sure you can guess, LTM stands for Long Term Memory. It's a large variable that records all of the headlines in a runthrough of the program. This variable resets every
time you restart the program. This variable prevents the headline from ever being shared again (until you start the program again).

SmartTime:
SmartTime is a system designed to reduce the internet data used in order to maximize the headlines recieved in a given time and to reduce the data wasted on recieving data from sites. 
Every time the system does not recieve a new hit in a runthrough of all of the sites, it will add on time to the clock, so it checks sites less frequently. Every time the program finds
a new hit on any of its sites, it will remove time from the clock, reducing the time it waits before checking sites. Adjusting this variable in settings changes that interval that it 
adds/subtracts. Changing this variable to 0 will disable this system.

WaitTime:
This one is very self-explanatory. This is the time the system will wait between checking sites. This is another precaution meant to reduce the flow of data. Increase or decrease
to affect the frequency of checking sites. This is the variable that SmartTime modifies while the program is running. 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
One last thing to know is that this program will give you an HTML error every once in a long while. This is not a fault of my programming nor is it avoidable. It is the equivalent of a 
website not loading on google. Glitches happen with the web.





