Steps required for the setup

- python/3/py -m venv {name of environment(env)} (It will create environment)
- ./{name of environment(env)}/bin/activate (It will activate environment) (for windows)
- source {name of environment(env)}/bin/activate (It will activate environment) (for mac/linux)
- pip3 insatll -r requirement.txt (To install all dependencies)


- Command for creating django -> django-admin startproject {name of tha project} (Skip this part if it is already created)

- cd {name of the project}
- python/3/py manage.py runserver
(It will start server on port 8000) (http://localhost:8000 | http://127.0.0.1:8000)