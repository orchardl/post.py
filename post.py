import requests
import random
import threading

userNames = ['snowballzclub', 'wilsongarbozana', 'andrieandcarney', 'mariamadrugadal', 'familia896543', 'dannytootwo2', 'facepalm334', 'faceplan2', 'frankrodney', 'frankierodd', 'williebon', 'flapsjacks2', 'reedandco', 'ronaldandco', 'companyparty336', 'seventytwo77', 'ninerniner787', 'mooremeatplz', 'frankiesinatra', 'perezfamilia', 'familiamadrugal', 'familiasanchez236t', 'thebdnn', 'smithster1', 'smoot4565', 'joggertothemax', 'cantcatchme223', 'faceburt33', 'john.williams955', 'eatmydust978', 'jnj123', 'bormorg12', 'abc9995', 'thebigbang999', 'rob1bob', 'rob2bob', 'bigerbanger', 'yourmoment234', 'sofardar33', 'nineteen19', 'twelve12', 'neverguess99', 'brokentooth19', 'jackandjill1', 'jjnin93', 'toothnnail12', 'thirteen14', 'cortex3', 'smaillmail1', 'threebirds1', 'adamsfamily123', 'harrisb1', 'stevens1', 'robinson1', 'lewis123', 'shobdo12', 'moonstar1', 'startsmoon2', 'allthesingle9', 'niner1niner', 'daniellewis', 'lindajones', 'lisawhite', 'andygriffiths1', 'corbynblue123', 'younger1', 'allenjoines1', 'wrightlight1', 'sandragreen2', 'carrietaylor', 'smallhall1', 'knightlight', 'knight1', 'coxsox', 'paulandrew', 'paulandrew1', 'joshuacorbin1', 'baileysummers1', 'brownclown3', 'small1wall', 'yakessnakes', 'zellykelly', 'chase1294949', 'small3call', 'smokes908', 'brokenglass9', 'greentee2', 'smallwallball3', 'greensocks9', 'wallball1995', 'greensocks23', 'eatthegreen43', 'yakessnakes', 'angela0987', 'onetwothree333', 'peterson998', 'pertersberg3', 'quailmail3', 'ratsnc2']
userNamesL = 99

firstNames = ['Jane', 'Hannah', 'Kathryn', 'Maria', 'Samuel', 'Benjamin', 'Frank', 'Dale', 'Joseph', 'Mary', 'Jordan', 'Jill', 'Martin', 'Brown', 'John', 'Robert', 'Roy', 'Greg', 'Karl', 'Craig', 'Bill', 'Venessa', 'Jared', 'Jack', 'Bob', 'Steven', 'Adam', 'Eve', 'James', 'Michael', 'William', 'David', 'Richard', 'Thomas', 'Charles', 'Christopher', 'Daniel', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen', 'Nancy', 'Lisa', 'Betty', 'Margaret', 'Sandra', 'Ashley', 'Kimberly', 'Emily', 'Donna', 'Michelle', 'Dorothy', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Paul', 'Andrew', 'Joshua', 'Kenneth', 'Kevin', 'Brian', 'George', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 'Gary', 'Nicholas', 'Eric', 'Larry', 'Justin', 'Scott', 'Brandon', 'Rebecca', 'Sharon', 'Laura', 'Cinthia', 'Kathleen', 'Amy', 'Shirley', 'Angela', 'Helen', 'Anna', 'Brenda', 'Pamela', 'Nicole', 'Emma']
firstNamesL = 100

lastNames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Adams', 'Wilson', 'Burton', 'Harris', 'Stevens', 'Robinson', 'Lewis', 'Walker', 'Payne', 'Baker', 'Owen', 'Holmes', 'Chapman', 'Webb', 'Allen', 'Jones', 'Davidson', 'Foster', 'Matthews', 'White', 'Griffiths', 'Knight', 'Corbyn', 'Young', 'Evans', 'Smith', 'Wright', 'Jenkins', 'Green', 'Hughes', 'Taylor', 'Hall', 'Anderson', 'Armstrong', 'Cox', 'Atkinson', 'Bell', 'Carter', 'Cole', 'Collins', 'Dawson', 'Bailey', 'Ball', 'Dixon', 'Edwards', 'Brown', 'Clarke', 'Yakes', 'Zelly', 'Zouch', 'Fisher', 'Fletcher', 'Ford', 'Fox', 'Gibson', 'Grahm', 'Grant', 'Gray', 'Sallow', 'Fernsby', 'Villin', 'Miracle', 'Dankworth', 'Relish', 'Loughty', 'Birdwhistle', 'Berrycloth', 'Palmer', 'Peterson', 'Quill', 'Quintrell', 'Ratliff', 'Stewart']
lastNamesL = 100

emails = ['@gmail.com', '@yahoo.com', '@aol.com', '@hotmail.com', '@outlook.com', '@gmail.com']
emailsL = 6

chars = ['.', '_', '-', '+', '']
charsL = 5

url = 'https://ddcgroup.pl/@66/safe.php'

def worker(num):

    for n in range(100):
        randomUN = random.randint(0, userNamesL-1)
        randomFN = random.randint(0, firstNamesL-1)
        randomLN = random.randint(0, lastNamesL-1)
        randomE = random.randint(0, emailsL-1)
        randomNum = random.randint(10, 1999)
        randomNum2 = random.randint(10, 199)
        randomChar = random.randint(0, charsL-1)

        theEmail = firstNames[randomFN] + chars[randomChar] + lastNames[randomLN] + str(randomNum2) + emails[randomE]
        thePassword = userNames[randomUN] + str(randomNum)

        #print(n, i)
        #print(theEmail)
        #print(thePassword)

        form_data = {
            'location': '',
            'ck': theEmail,
            'cknow': thePassword,
            'password2': '',
            'store': '1',
            'signin': 'Sign in'
        }
        response = requests.post(url, data=form_data)
        #print(response.text)
        #print('\n')


threads = []

for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
