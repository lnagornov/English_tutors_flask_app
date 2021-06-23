import json

def get_data_from_db(option='all'):
    '''Read data from database (json file) and returns a dict of data.
    1. Mode by default is option='all' returns dict with all data.
    2. option='tutors' returns dict with only about tutors.
    3. option='goals' returns dict with only about goals.
    4. option='days_of_week' returns dict with days of the week in rus and eng
    5. option='time_for_practice' returns dict with days.
    '''
    if option not in ('all', 'tutors', 'goals', 'days_of_week', 'time_for_practice'):
        raise AttributeError

    with open('db.json', encoding='utf-8') as f:
        db = json.load(f)
        if option == 'all':
            return db
        elif option == 'goals':
            return db[0]    
        elif option == 'tutors':
            return db[1]
        elif option == 'days_of_week':
            return db[2]
        elif option == 'time_for_practice':
            return db[3]


def add_goal_to_tutor(goal, tutor_id):
    '''Appends a goal to a tutor in database.
    Requies goal->str and tutor_id->int
    '''
    all_tutors = get_data_from_db(option='tutors')
        
    with open('db.json', encoding='utf-8') as f:
        db = json.load(f)
        all_tutors = db[1]
        for tutor_info in all_tutors:
            if tutor_info['id'] == tutor_id:
                if goal not in tutor_info['goals']:
                    tutor_info['goals'].append(goal)
                break
    with open('db.json', 'w', encoding='utf-8') as w:
        json.dump(db, w, ensure_ascii=False, indent=4, separators=(',', ': '))
        print(f'Goal - {goal} has been added to {tutor_info["name"]} with id {tutor_id}')



def is_request_in_db(request):
    '''Returns True if request already in database, otherwise returns False'''
    with open('users_requests.json', encoding='utf-8') as f:
        db = json.load(f)
        if request in db:
            return False
        return

def save_request(request):
    '''Saves user request into json file'''
    with open('users_requests.json', 'a', encoding='utf-8') as f:
        json.dump(request, f, ensure_ascii=False, indent=4, separators=(',', ': '))
        print(f'Request - {request} has been added to users_requests.json')
    pass