# Millenium Falcon Challenge

The Death Star - the Empire's ultimate weapon - is almost operational and is currently approaching the Endor planet. The countdown has started.

Han Solo, Chewbacca, Leia and C3PO are currently on Tatooine boarding on the Millennium Falcon. They must reach Endor to join the Rebel fleet and destroy the Death Star before it annihilates the planet.

The Empire has hired the best bounty hunters in the galaxy to capture the Millennium Falcon and stop it from joining the rebel fleet...


# Prerequisites
*In this tutorial, we will suppose that Python 3.10 or above is installed on your machine, if not follow the links below:*
1. *https://www.python.org/downloads/*
2. *https://docs.python.org/fr/3.10/installing/index.html*

# Installing the package



## Install with pip

First, get the package from the latest release [here](https://github.com/RaymondSoun/millenium-falcon-challenge/releases/latest)

Create a new folder for the project and a virtual environment
```
$ mkdir <path/to/project>
```
```
$ cd <path/to/project>
```
Create a virtual environment
```
$ virtualenv -p python3 myvenv
```
And activate it:
```
$ source myvenv/bin/activate
```

Install the package with the following command (the name may change depending on the release version):
```
$ pip install mfc-0.1.0-py3-none-any.whl
```

## Install with docker

...

# Using the software

## Basic commands

To caclulate the odds with the CLI use the following command:

```
$ mfc solve path/to/millennium-falcon.json path/to/empire.json
```
Make sure that the universe.db in the millennium-falcon.json exists and is correct.

To launch the local web server :
```
$ mfc serve path/to/millennium-falcon.json
```
This will create a basic web server to calculate the odds via a web interface.

You can also use the following command if you need help:

```
$ mfc --help
```
## Sample data
You can use the following sample data to test the app

[universe.db](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/universe.db?raw=true)

[millennium-falcon.json](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/millennium-falcon.json?raw=true)

[empire.json](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/empire.json?raw=true)