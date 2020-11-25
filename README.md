# Project Name - Pied Piper 
Pied Piper is a platform that contains all club related opportunities/leadership positions 

Our platform has two main functions:
1. It allows club representatives looking to hire to post available job positions at their clubs
2. It allows IE Students to search among the available positions to find their ideal job



# INSTALLATION
To be able to run our program, make sure you have the following things installed:

  1. Python programming language - It will work in all versions between 3.6 and 3.8. (Despite Python launching 3.9 recently, libraries are not getting updated, so we would advise our users to stick to version 3.6 or 3.7) 
  2. Libraries - In order to run our program, we make use of the following 2 libraries: heapq_max and re  
    i) Re is an inbuilt library which comes as a part of the standard library module   
    ii) heapq_max on the other hand needs to be downloaded in order for the program to run.   
        To download the library, either use the GUI in your IDE or go to your terminal and type the following command 
    ```
    pip install heapq_max
    ```
  Now that we have the required libraries set up. Go the the file named $app.py$ and execute the program through your IDE or go to the terminal and type the following command   
  For mac - ```python3 app.py```  
  For Windows - ```python app.py```  

# USAGE
After a user enters our platform, they will be welcomed and asked what their intentions are: Posting a new job, searching for a job, or closing a job position.
After being validated, this choice will conduct the user onto a different function. We will now go through the three different choices


1. Posting a new job
Our job inserting function has the purpose of enabling club representatives to upload available job positions. It will first ask the user to type in the following information about the job he wants to post: 

  A job title, the position, the club, the location (Madrid, Segovia or Online), an email address, the time of the year (spring or fall), and a job description.
  
  Once all of this information has been inserted and validated by our algorithm, the job will be added into our default jobs function, which is responsible for storing all of   the available job positions. The user will receive a final message confirming that the job has been correctly uploaded, as well as the information of the job itself.


2. Searching for a job
Our job searching function has the purpose of showing IE students the available job positions that best match their preferences.
It will start by displaying a list with all available positions showing only unique titles. 

  The user will then be asked:
  - The position he is interested in.
  - The location he would like to work in (Madrid, Segovia or Online).
  - The time of the year (spring or fall).
  
  With these three choices in mind, our algorithm will go through all available job positions inside the job default function. It will sort the jobs so that those that are     more compatible with the student (they contain more priorities) will be shown first. 
  The jobs that share no priorities will be filtered out.
  The user will get the sorted list of compatible jobs as an output.


3. Deleting an existing job
Our job deleting function has the purpose of enabling club representatives to remove an existing job post that has already been filled in.
First, the user will be shown a list of all available job positions, which will be extracted from the default jobs function.
Then, he will be asked the name of the job he wishes to remove.
After validating his input, the function will remove the job from the storage function.
The user will be shown a message saying that the job removal was successful.



# SOME EXTRA INFORMATION ABOUT THE CODE
In order to carry out our objective, we have used the following data structures:

  1. Hash Tables - Used to store all details regarding the opportunities 
  2. Heaps - used to find the most appropriate opportunity for the user based on their preferences  

And the following Algorithms:

  1. Insertion 
  2. Deletion 
  3. Searching 


# CREDITS
The authors for this project are:   
Abdul Salam  
Anshumaan Ravi  
Isabel Ordovas  
Natalia Caceres   
Natalia Nowak   




