
# Millenium Falcon Challenge

  

The Death Star - the Empire's ultimate weapon - is almost operational and is currently approaching the Endor planet. The countdown has started.

  

Han Solo, Chewbacca, Leia and C3PO are currently on Tatooine boarding on the Millennium Falcon. They must reach Endor to join the Rebel fleet and destroy the Death Star before it annihilates the planet.

  

The Empire has hired the best bounty hunters in the galaxy to capture the Millennium Falcon and stop it from joining the rebel fleet...

  
  

# Prerequisites

*In this tutorial, we will suppose that Python 3.10 or above is installed on your machine, if not follow the links below:*

1.  *https://www.python.org/downloads/*

2.  *https://docs.python.org/fr/3.10/installing/index.html*

  

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

  
Run the following commands to install the frontend project with Docker:

  
```
$ docker pull raymond93/millenium-falcon-challenge-back
```



```
$ docker run -p 5000:5000 raymond93/millenium-falcon-challenge-back
```

  

The server should now be started with the default settings (millenium falcon file and universe.db).
  

# Using the software

  

## Basic commands
### With host installation
  

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

### With docker installation
To caclulate the odds with the CLI on docker use the following command:

```
$ docker run -p 5000:5000 --rm -v '<absolute/path/to/local/empire.json>':/data/empire.json  millenium-falcon-challenge-back mfc solve millennium-falcon.json empire.json
```
You can also provide millennium-falcon.json and a universe.db in a folder like so:

```
$ docker run -p 5000:5000 --rm -v '<absolute/path/to/folder>':/data/ millenium-falcon-challenge-back mfc solve millennium-falcon.json empire.json
```
Make sure the files are named correctly (millennium-falcon.json, empire.json, universe.db)

To start the local web server, you can execute
```
$ docker run -p 5000:5000 --rm -v '<absolute/path/to/folder>':/data/ millenium-falcon-challenge-back mfc serve millennium-falcon.json
```
Make sure you include the files named correctly (millennium-falcon.json and universe.db)

## Sample data

You can use the following sample data to test the app

  

[universe.db](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/universe.db?raw=true)

  

[millennium-falcon.json](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/millennium-falcon.json?raw=true)

  

[empire.json](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/empire.json?raw=true)
