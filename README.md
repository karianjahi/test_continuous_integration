# poblano_count_words_app
This app counts the number of words in a sentence (or text)

You must install `pytest`, `pytest-cov` and `coverage` using `pip install`

To test the code just type: `pytest`

To measure coverage type: `pytest --cov`

To output coverage into a html `coverage html`

The immediate command above creates a folder known as `htmlcov`. Inside this folder exists the file `index.html`

You can then open the above html file using a browser of your choice e.g. `firefox htmlcov/index.html`


# Make the app pip-installable
- Traditionally, to access the python scripts from outside the App, we usually add a file called `__init__.py`. This file makes our app a package.

- To make our `poblano...app` pip installable, we do the following:
	- create `__init__.py` file
	- move all tests to their own folder called `tests`
	- to make sure that the tests will run, we need to add an empty file known as `__init__.py` in the tests folder
	- We now need to move the main script file to a folder of the same name as the project folder (not because it is a must that they should have the same name but it is a tradition)
	- We need to create another `__init__.py` file inside the newly created folder above
	- Add a file called `setup.py`. This is the file that renders our app (package) pip-installable.\
	- Make sure you add a `requirements.txt` file. To create it, type `pip freeze > requirements.txt`

# CONTINUOUOS INTEGRATION
The aim of Continuous Integration (CI) is to make sure that github looks at our code and gives a thumbs-up that the code is okay in terms of especially automated tests.

## Procedure for CI:
- Create a repo on Github --> Done
- Clone the repo --> Done
- Build the code ---> Done
- Push the code ---> Done
- Create a badge that tells users of our code (us included) that the tests therein passes.
- The badge is passed by github actions. Github creates a virtual environment and based on the instructions that we give, it creates a virtual machine that runs our code before it can be pushed. 
- If there is any problem with our code, the github actions will fail and we should be able to see it.
- **How do we do this?**
	1. Create a folder in our main project called `.github`
	2. Inside the `.github` folder, we create a workflow using a yaml file with instructions on how to build the virtual machine, install all requirements and run our code.
		- If our code is okay, github gives us a green color.
		- If not, it is a red!
- In our case, we want to implement our continuous integration in a brand new branch.
- We call this branch `continuous_integration`.
- To create a new branch in github: 
  - `git checkout -b <branch name>`
  - In our case: `git checkout -b continuous_integration`
