from datetime import date

def getUsers():
    users = [
    {
        'id':1001,
        'username':'jorge24',
        'register_date':date(2002, 12, 31),
        'photo_url':'https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&fl=progressive&q=70&fm=jpg',
        'problems_history':[
            {
                'problem_id':100,
                'date_solved':date(2024, 2, 9),
                'score':90
            },
            {
                'problem_id':101,
                'date_solved':date(2024, 2, 10),
                'score':60
            },
            {
                'problem_id':102,
                'date_solved':date(2024, 2, 11),
                'score':20
            }
        ],
    },
    {
        'id':1001,
        'username':'carlossalvaje',
        'register_date':date(2002, 12, 31),
        'photo_url':'https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&fl=progressive&q=70&fm=jpg',
        'problems_history':[
            {
                'problem_id':100,
                'date_solved':date(2024, 2, 9),
                'score':90
            },
            {
                'problem_id':101,
                'date_solved':date(2024, 2, 10),
                'score':60
            },
            {
                'problem_id':102,
                'date_solved':date(2024, 2, 11),
                'score':20
            }
        ],
    }
]
    return users


def getUser(username):
    return next((user for user in getUsers() if user['username'] == username), None)

#jorge = getUser("jorge24")
#print(jorge['username'])
