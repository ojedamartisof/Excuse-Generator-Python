import random

frase = []

who = ['the dog','my granma ','his turtle','my bird']
action = ['pissed ','crushed ','broked ','eat ']
when = ['when i finished','during my lunch','right in time','before de class']
what = ['my  computer ', 'my clothes ', 'my shoes ', 'my food']

def create_excuse():
    frase = who[random.randint(0,3)] + action[random.randint(0,3)] + what[random.randint(0,3)] + when[random.randint(0,3)]
    print(frase)

create_excuse()
