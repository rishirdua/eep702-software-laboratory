EEP702: Software Laboratory, IIT Delhi (Fall 2013 Semester)
===========================================================


Disclaimer:
-----------
- The questions have been adapted from the EEP702 Software Laboratory course (Fall 2013 semester) at IIT Delhi. Most of the questions are not exactly the same as in the course. I have added/removed/modified certain parts for my practice.
- The codes and documentation in this repository might have been modified from my original submission for the EEP702 software laboratory course.


Assignment 1: Reverse Spiral and String Matching
------------------------------------------------
Language: Java
Problem Statement:
- Print matrix (M) elements in reverse spiral order ie., starting from the centre element, print all the elements in spiral order until the first element M[0][0] is reached. Matrix M is of order n where n is odd
- Match two strings containing wildcard characters ’?’ and ’*’ . ’?’ denotes no or exactly one character and ’*’ denotes no or many characters.


Assignment 2: String manipulation
---------------------------------
Write a program (called NumOfOccurrences) to find how many times a substring s2 occurs in a bigger string s1
Let 'file.txt' be a text file containing string s1 of alphanumeric characters.

- Invocation 1: $ NumOfOccurrences s2\\
only one string is given and it is understood as s2,s1 is hardcoded in the program
- Invocation 2: $ NumOfOccurrences s1 s2
both strings are specified on the command line and the sequence determines which s s1 and which is s2. Find the total number of occurrences of a substring s2 to be entered by the user.

Logically divide the string s1 into 'm' number of even partitions and parallely search to count the total number of occurrences of s2 parallely using threads, where 'm' is the number of threads to be entered by the user. Let the length of string s1 [denoted as len(s1) ] be n1 and number of threads be m, then the length of each partition would be (n1/m) and n2 = len(s2) ( < (n1/m)) During runtime, print using an external subroutine StringPrint(*char s) the 'id' of thread in which the substring s2 is found. Each thread will find the occurrence in its local string partition. IPC and message queues can be used for communication among threads, and finally print the total number of occurrences of s2 in s1.

The output of StringPrint(.) looks moreover like this:\\
<current UTC time> <id of thread where s2 is found> [n times]\\
Total embeddings of s2 in s1 = < \# >\\

- Repeat the above using C

- Profile the code in Section a and compare its size with the source code in previous part.

Language: Bash, C

Assigment 3: Ubuntu Weather App
-------------------------------

Develop an ubuntu app which can accomplish following two tasks:
- Forecasting next few days weather conditions
- Keep record of past few days' weather conditions (max 30 days) in to your database and show it as a strip chart which has a rewind / fast fwd button.
 
Use tcl/tk for the GUI to interact with the user and python for other operations. The user will be asked to enter name of a place for which weather conditions have to be forecasted, the number of days (n) for which to show information, and to press a button to decide whether to forecast or tell about the past n days weather conditions. Use MySQL as database. Max 5 days' information need to be recorded. Make use of yahoo api for weather forecasting info. Develop html documentation using Doxygen. Give user an option to provide details of the place either by specifying name of that place or manually entering geographical location (lat/ long).

Language: TCL/TK, SQL


Assignment 4: Library Management
--------------------------------
Write a program in Java only for Library Management.

Use a text file to store the following information about the books available in the library.
(Title of the book) (Author name) (Publication) (Edition)
Read from the file and store them as array of objects. Provide user the functionality to search for some books based on Book title, author name, publication or any combination of 
these.

Add the Library Incharge Login functionality to above program which enables him to add or remove any book from the library. The changes must be reflected in the Library record and all student accounts as well.

Add the Student Login functionality to above program to keep a record of the books issued to each student along with the date of issue.

Add the functionality to above program to calculate total fine imposed in case any user fails to deposit the issued book within a period of 1 week.

Language: Java


Assignment 5: Shell Scripting
-----------------------------
The inputs are name of the folder to be opened and the extension type of the files and these are to be passed through commandline.
sh <scriptname><foldername><extension type>
Open the user given folder and search for the subfolders with names having only small letters and without spaces. In these subfolders, write the names of files that have the user given extension into “match.txt” in the following format.
<subfolder matching pattern>
<Files in that subfolder matching extension >
<next sufolder matching pattern>...and so on.
If the given extension is a c or sh, execute the files assuming the files require no runtime or compile time arguments.
Convert all the capital letters to small case and remove blank spaces in the names of all the subfolders of the given folder.
Rename gif files into png extension in the subfolders which match pattern when the extension type is given gif.

Language: Bash


Assignment 6: Partition Problem
-------------------------------
There are N packets, each with one or more candies. There are K students among which the packets have to be distributed. (Assume K less N for all cases). The parameters N and K have to be provided by the user at run-time. Each student gets only one packet. The number of candies in various packets are (x1, x2, x3,....xk ) , where xi denotes the number of candies in the ith packet. Find the number of triplets (x1, x2, x3) possible such that sum of the candies (x1 + x2 + x3) is even.

Divide the packets into two parts (p1 and p2) such that the difference (|p1-p2|) is minimum, where p1 and p2 are the total number of candies in part 1 and part 2 respectively.

Language: Java


Assignment 7: Sentiment Analysis
--------------------------------
You are given a text file which contains random facebook status. You have to do sentiment analysis of those posts on the basis of
positive,negative and neutral feelings. To differentiate between feelings, create (hardcode) a dictionary having various positive and
negative words. Match whether a post has any of those words and if it has, it gets counted into the respective category. Also Include emoticons (for ex. :) for positive and :( for sad). Consider a post having neither positive nor negative feelings as neutral.

Tasks:
- Count the number of posts with each kind of ‘feeling’ for a given hour
- Make a table with entries “feeling” and “its count in terms of posts in a given hour
- For each hour,normalize this counted data on the scale of [-1,0,1] i.e. assign weight of -1 to negative feeling, +1 to positive feeling , 0 to neutral feeling and adding all, divide result by total number of posts in that hour.From this calculated data, plot a graph with hour as X-axis and normalized feeling value as Y-axis.
- Find the respective hours in which most number of posts arrived for each category of feeling.
- Given any two “geographically separate” places, compare the number of posts in those places containing different category of feelings.
- Extract the location of the places in the post and give a graphical representation with the place as X-axis and the normalized mood value for the whole file on Y-axis.
- Plot the overall feelings of a location normalized against all other locations

Language: Python


Assignment 8: QT GUI Design
---------------------------
Design a user interface(GUI) in Qt. The user will be asked to enter a number in numeric
(say, 55) and will be provided a button named “Convert to text”. On pressing this button, the
entered number should be displayed in words (fifty five).

Add one more feature to the above GUI, which will enable user to enter a number in text
(fifty five). Add one button named “Convert to Number”, on pressing which the entered
number in words will be shown in numeric digits (55).

Language: QT


Assignment 9: Inline Assembly in C
----------------------------------
Given two integers, write a time efficient c code, that spends as less time in memory access and more in calculations as possible, to get their GCD and LCM. Use directives for conditional compilation of code as follows.
Identifier Status: 1 -> GCD
Identifier Status: 0 -> LCM
Find the critical parts of code that consume more percentage of time and replace those parts with inline assembly coding to optimize speed and compare the time profiling for both codes.
- Find the most significant non zero bit position for largest of the two given integers using pure c code and inline assembled c code and show which one is faster.
- Convert the given integer(assumed to be angle in degrees) to radians and find the floating cosine value with pure c and inline assembled c and determine fastest one.

Languages: C, Assembly


Assignment 10: Connected component labelling
--------------------------------------------
- There is a mass of land containing some finites number of water bodies. Let the piece of land be represented by a 2-D matrix, whose each cell represents a unit area. Value '0' of a cell denotes
that it comes under land area and '1' denotes that it comes under water body. If the cells connected by a 4-point connectivity forms a single water body, find the total number of water bodies.
- If the cells connected by a 8-point connectivity forms a single water body, find the total number of water bodies.
- Label the water bodies so that if user specifies a cell (m,n), the program must tell whether it comes under a water body.

Language: Python


Contribute:
-----------
- Source Code: https://github.com/rishirdua/eep702-software-laboratory
- Project page: http://rishirdua.github.io/eep702-software-laboratory


Licence:
--------
This project is licensed under the terms of the MIT license. See LICENCE.txt for details