import heapq_max
import re


def user_welcome():
    print('Welcome to Pied Piper -- A one stop place for you to keep track of all available opportunities!')
    print('\nAre you a job seeker or a job poster?\nEnter 1 for job seeker \nEnter 2 for job poster\nEnter 3 to close a job position\nEnter 4 to quit')


def job_search(available_jobs):
    # Job Seeker needs to input position name, Location, Time period
    print("Here is a list with the available job positions:")
    position_list = []
    for key in available_jobs.keys():
        position_list.append(available_jobs[key][0])
    print(list(set(position_list)))
    name = input(
        "Please enter the position from the list above that you would like to have:").strip().lower()
    while name not in position_list:
        print("We are sorry, but it looks like the position you entered is not available, please try again")
        name = input(
            "Please enter the position from the list above that you would like to have:").strip().lower()

    location = input(
        "Please select a location among the following options: Madrid/Segovia/Online:").strip().lower()
    while location != 'madrid' and location != 'segovia' and location != 'online':
        print("We are sorry, but it looks like the location you entered is not available, please try again")
        location = input(
            '\nPlease enter the location - Madrid/Segovia/Online: ').strip().lower()

    time = input(
        "Please enter your preferred time - Spring/Fall:").strip().lower()
    while time != 'spring' and time != 'fall':
        print("We are sorry, but it looks like the time you entered is not available, please try again")
        time = input(
            '\nPlease enter the time period - Spring/Fall: ').strip().lower()

    user_preference = {name, location, time}
    print()
    jobs_heap = []
    for jobs, conditions in available_jobs.items():
        conditions_set = set(conditions)
        priority = len(user_preference & conditions_set)
        heapq_max.heappush_max(jobs_heap, (priority, jobs))

    for i in range(len(jobs_heap)):
        if jobs_heap[i][0] > 0:
            print('Option', i+1, ':',
                  str(available_jobs[jobs_heap[i][1]])[1:-1], '\n')


def email_check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
        return False


def job_insert(available_jobs):
    print('You are posting a job!')
    print('Please enter the following details: ')
    # Job Poster needs to input position name, Location, Description of the position, Contact Info, Time period, name of club
    keys = [key for key in available_jobs.keys()]

    title = input(
        'Please enter the position name in the following format: Name of Club + Position Name Eg- Debate Club President: ').strip().lower()
    while title in keys:
        print('Position title already exisits. Enter a different one!')
        title = input(
            'Please enter the position name in the following format: Name of Club + Position Name Eg- Debate Club President: ').strip().lower()

    position = input('\nPlease enter the position: ').strip().lower()
    club = input('\nPlease enter the club name: ').strip().lower()

    location = input(
        '\nPlease enter the location - Madrid/Segovia/Online: ').strip().lower()
    while location != 'madrid' and location != 'segovia' and location != 'online':
        print("We are sorry, but it looks like the location you entered is not available, please try again")
        location = input(
            '\nPlease enter the location - Madrid/Segovia/Online: ').strip().lower()

    email = input('\nPlease enter the email address: ').strip().lower()
    while not email_check(email):
        print("We are sorry, but it looks like the email address is not valid, please try again")
        email = input('\nPlease enter the email address: ').strip().lower()

    time = input(
        '\nPlease enter the time period - Spring/Fall: ').strip().lower()
    while time != 'spring' and time != 'fall':
        print("We are sorry, but it looks like the time you entered is not available, please try again")
        time = input(
            '\nPlease enter the time period - Spring/Fall: ').strip().lower()

    description = input('\nPlease enter the job description: ').strip().lower()

    values = [position, club, location, time, email, description]
    available_jobs[title] = values
    print('\nThe position has been added!\n')
    print(title, ':', str(values)[1:-1])


def job_delete(available_jobs):
    print('You are deleting a job!')
    print('These are the available job positions:')
    keys = [key for key in available_jobs.keys()]
    print(str(keys)[1:-1])
    position = input(
        'Please enter the job position from the above list: ').strip().lower()
    while position not in keys:
        print('Invalid deletion. Please enter a valid position to be deleted')
        position = input(
            'Please enter the job position from the above list: ').strip().lower()
    del available_jobs[position]
    print('The', position, 'job has been deleted!')


def default_jobs():
    available_jobs = {}
    # Job Poster needs to input position name, Location, Description of the position, Contact Info, Time period, name of club
    available_jobs['coding club coordinator'] = ['club coordinator', 'coding club', 'madrid', 'spring',
                                                 'iecodingclub@gmail.com', 'you will be responsible for organising events and workshops']

    available_jobs['music club coordinator'] = ['club coordinator', 'music club', 'online', 'spring',
                                                'iemusicclub@gmail.com', 'you will need to create new events and work on buidling a music team at IE']

    available_jobs['debate club coordinator'] = ['club coordinator', 'debate club', 'segovia', 'spring',
                                                 'iedebateclub@gmail.com', 'you will need to organise debates/discussions for students and collaborate with other clubs to organise events']

    available_jobs['excursion club graphic designer'] = ['graphic designer', 'excursion club', 'madrid', 'spring',
                                                         'ieexcursionclub@gmail.com', 'you will need to design posters and other promotional materials for the club']

    available_jobs['stork graphic designer'] = ['graphic designer', 'the stork', 'online', 'spring',
                                                'ieustorkb@gmail.com', 'you will need to design posters and other promotional materials for the Stork']

    available_jobs['eco club president'] = ['club president', 'eco club', 'segovia', 'spring',
                                            'ieecoclub@gmail.com', 'we are looking for people to take over the leadership board for the Eco Club Segovia branch']

    return available_jobs


def check_options(available_jobs):
    try:
        option = input('\nPlease enter your answer: ')

        while option != '1' and option != '2' and option != '3' and option != '4':
            print('Incorrect input. Please enter again')
            option = input('\nPlease enter your answer: ')
        if int(option) == 1:
            job_search(available_jobs)
        if int(option) == 2:
            job_insert(available_jobs)
        if int(option) == 3:
            job_delete(available_jobs)
    except ValueError:
        print("\nWe are sorry, it appears you did not enter the right characters, please try again")
    except:
        print("\nOops! Something went wrong, please try again later")


def main():
    user_welcome()
    available_jobs = default_jobs()
    check_options(available_jobs)


main()
