# Project Name - Pied Piper 
Pied Piper is a platform that contains all club related opportunities/leadership positions 

Our platform has two main functions:
1. It allows club representatives looking to hire to post available job positions at their clubs
2. It allows IE Students to search among the available positions to find their ideal job



# INSTALLATION
In order to ensure output reproducibility, please see if the following conditions are met 
  1. Python programming language - version 3.6.10 (It will work in all versions above 3.6 until 3.8. Despite Python launching 3.9 recently, due to libraries not getting updated, we would advise our users to stick to version 3.6 or 3.7) 
  2. Libraries - In order to run our program, we make use of the following 2 libraries heapq_max and re
    i) Re is an inbuilt library which comes as a part of the standard library module 
    ii) heapq_max on the other hand needs to be downloaded in order for the program to run. 
    In order to download the library, either use the GUI in your IDE or go to your terminal and type the following command 
    ```python
    pip install heapq_max
    ```
    

# USAGE
After a user enters our platform, he will be welcomed and asked what his intentions are: Posting a new job, searching for a job, or closing a job position.
After being validated, this choice will conduct the user onto a different function. We will now go through the three different choices:

1. Posting a new job:
Our job inserting function has the purpose of enabling club representatives to upload available job positions.
It will first ask the user to type in the following information about the job he wants to post: 
a job title, the position, the club, the location (Madrid, Segovia or Online), an email address, the time of the year (spring or fall), and a job description.
Once all of this information has been inserted and validated by our algorithm, the job will be added into our default jobs function and stored as a hash table.
This default jobs function is responsible for storing all of the available job positions.
The user will receive a final message confirming that the job has been correctly uploaded, as well as the information of the job itself.

2. Searching for a job:
Our job searching function has the purpose of showing IE students the available job positions that better match their preferences.
It will start by displaying a list with all available positions, filtering out any duplicates.
The user will then be asked in what position he is interested in.
He will also be asked the location he would like to work in (Madrid, Segovia or Online), and the time of the year (spring or fall).
With these three choices in mind, our algorithm will go through all available job positions inside the job default function, filtering out those who share none of the users requests about position, location and time.
It will then sort the rest of jobs, in a way that those that are more compatible with the student (they contain more priorities) will be shown first.
The user will get the sorted list of compatible jobs as an output.

3. Deleting an existing job:
Our job deleting function has the purpose of enabling club representatives to remove an existing job post that has already been filled in.
First, the user will be shown a list of all available job positions, which will be extracted from the default jobs function.
Then, he will be asked the name of the job he wishes to remove.
After validating his input, the function will remove the job from the storage function.
The user will be shown a message saying that the job removal was successful.

# CREDITS




