# weekly-meals
This Project hosts a web app to plan the meals of the week and send the plan to your family

## Setup

### Python

Install Python3

```shell
sudo apt update
sudo apt install python3
```

Install pip3

```shell
sudo apt-get install python3-pip
python3 -m pip install --user --upgrade pip
```

#### Python Virtual Environment

Install venv

```shell
sudo apt-get install python3-venv
```

The scripts in this folder are designed to be set up using a Python virtual environment (`venv`). The first time you want to set up the application on Linux, execute the steps below on a shell:

```sh
# Set up a virtual environment
python3 -m venv .venv

# Activate it
. .venv/bin/activate

# Install necessary packages and upgrade
pip install -r requirements.txt --upgrade
```

Please do _not_ use `sudo` within a virtual environment; it will not work as intended. Instead, set up your system correctly so that you do not need root access to run the script.

On Windows Command Prompt, the commands are slightly different:

```bat
REM Set up a virtual environment
python3 -m venv .venv

REM Activate it
CALL .venv\Scripts\activate.bat

REM Install necessary packages and upgrade
pip install -r requirements.txt --upgrade
```

For more information, e.g., using `venv` with Windows PowerShell, see the [official Python venv documentation](https://docs.python.org/3/library/venv.html).

To use the application again at a later time, you only need to perform the activation step.

#### Create/Update Requirements File
You can use the following code to generate a requirements.txt file:

```sh
pip freeze > requirements.txt
```

Instead of adding all the dependencies to the `requirements.txt` file, we can append only the packages we need to install without deppendencies:

```sh
pip freeze | grep "PACKAGE_NAME==" >> requirements.txt
```

To start intalling libraries again for fresh, you can update the dependencies list and then uninstall all the dependencies:

```sh
pip freeze > requirements.txt
pip uninstall -y -r requirements.txt
```

### Plant UML

The C4 diagrams are made using [PlantUML](https://plantuml.com/). 

To install the `plantuml` package in linux:

```console
sudo apt-get update
sudo apt-get install plantuml
```


## Build

### C4 diagrams

To build the diagrams, you only have to run the `plantuml` command:

```console
plantuml -tpng <path-to-the-files>
```

## References

- [The C4 model for visualising software architecture](https://c4model.com/)
- [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML)

## Test

#### Unittest

Test file simple template:

```py
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

To skip a test `@unittest.skip("<message>")` should be added in the source code before the test we want to skip:

```py
@unittest.skip("Should be refactored to work")
def test_to_skip(self):
```

To run the unit tests in the test root directory:

```shell
python3 -m unittest
```

You can select which is the root directory:

```shell
python3 -m unittest discover <test_directory>
```

To run the test in this project structure:

```shell
python -m unittest discover -s ./src/ -p "test_*.py" -v
```

To select the test of one test suite:

```shell
python3 -m unittest discover -k <test_suite_name> <project_source_dir>
```

To call one test case we use the test case name. To only run the test `dataset.utest.dataset_test.TestSuiteNNN.test_xxx` we use `test_xxx`:

```console
$ python -m unittest discover -s ./src/ -p "test_*.py" -v -k "test_xxx"
test_xxx (dataset.utest.dataset_test.TestSuiteNNN.test_xxx) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.230s

OK

```

To run the whole test suite NNN, we use the the test suite name `TestSuiteNNN`:

```console
$ python -m unittest discover -s ./src/ -p "test_*.py"  -v -k "TestSuiteNNN"
test_yyy (dataset.utest.dataset_test.TestSuiteNNN.test_yyy) ... ok
test_xxx (dataset.utest.dataset_test.TestSuiteNNN.test_xxx) ... ok
test_zzz (dataset.utest.dataset_test.TestSuiteNNN.test_zzz) ... ok

----------------------------------------------------------------------
Ran 3 tests in 3.036s

OK
```

## Run

### Flask

We can use the Flask development server that comes bundled with Flask in order to check that the code in the app.py file is working correctly.

Run the Flask Development Server to serve your Flask app:

```console
(venv) $ flask --app ./src/webui/app --debug run

 * Running on http://127.0.0.1:5000
 Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```

The --app argument specifies the Python file (without the .py extension) that contains the Flask application (app). The --debug argument specifies that the Flask Development Server run in 'debug' mode.

You can now view your app by navigating to <http://127.0.0.1:5000/weekly-meals-planner> in your browser of choice.

## Deployment

### Update Deployment

First go to the project folder published in Apacheand change its ownership and update the files pulling from the remote repo

```bash
cd /var/www/weekly-meals/
sudo chown -R pi:pi /var/www/weekly-meals
git pull
```

After that, activate the virtual environment and install all the dependences:

```bash
. .venv/bin/activate
pip install -r requirements.txt --upgrade
```

Then, change the apache folder ownership again and restart apache server

```bash
sudo chown -R www-data:www-data /var/www/weekly-meals
sudo systemctl restart apache2
```

