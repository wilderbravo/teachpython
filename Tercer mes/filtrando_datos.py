DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 15,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
    {
        'name': 'Ariosto',
        'age': 13,
        'organization': 'Python Organization',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Wilder',
        'age': 37,
        'organization': 'Python Organization',
        'position': 'Backend Developer',
        'language': 'javascript',
    },
]

# print(DATA)

all_python_dev = [worker["name"] for worker in DATA if worker["language"]=="python"]
all_javascript_dev = [worker["name"] for worker in DATA if worker["language"]=="javascript"]
adultos = [worker["name"] for worker in DATA if worker["age"]>=18]
menores_edad = [worker["name"] for worker in DATA if worker["age"]<18]
menores_edad_python = [worker["name"] for worker in DATA if worker["age"]<18 and worker["language"]=="python"]
adults_lambda = list(filter(lambda worker: worker["age"]>=18, DATA))
# adults_lambda = list(map(lambda worker: worker["name"], adults_lambda))
# old_people = list(map(lambda worker: worker | {"old": worker["age"]> 70}, DATA))
# print(menores_edad)
print(adultos)
print(adults_lambda)
# print(all_javascript_dev)

