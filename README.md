
# Millenium Falcon Challenge

  

The Death Star - the Empire's ultimate weapon - is almost operational and is currently approaching the Endor planet. The countdown has started.

  

Han Solo, Chewbacca, Leia and C3PO are currently on Tatooine boarding on the Millennium Falcon. They must reach Endor to join the Rebel fleet and destroy the Death Star before it annihilates the planet.

  

The Empire has hired the best bounty hunters in the galaxy to capture the Millennium Falcon and stop it from joining the rebel fleet...

# TLDR
If you want to use the tool as fast as possible you can launch the following commands:

## CLI

```
docker run -p 5000:5000 --rm -v $(pwd):/data/ raymond93/millenium-falcon-challenge-back mfc solve millennium-falcon.json empire.json
```

Make sure millennium-falcon.json, empire.json and universe.db are in your current working directory

## Web Interface 
```
docker run -p 5000:5000 raymond93/millenium-falcon-challenge-back
```

```
docker run -p 3000:3000 raymond93/millenium-falcon-challenge-front
```

You can now access the interface on [http://localhost:3000](http://localhost:3000)



# Prerequisites

*In this tutorial, we will suppose that Python 3.10 or above is installed on your machine, if not follow the links below:*

1.  *https://www.python.org/downloads/*

2.  *https://docs.python.org/fr/3.10/installing/index.html*

  

# Installing the package

## Install with docker

  
Run the following commands to install the frontend project with Docker:

  
```
docker pull raymond93/millenium-falcon-challenge-back
```



```
docker run -p 5000:5000 raymond93/millenium-falcon-challenge-back
```

  

The server should now be started with the default settings (millenium falcon file and universe.db).
  

## Install with pip

First, get the package (.whl file) from the latest release [here](https://github.com/RaymondSoun/millenium-falcon-challenge/releases/latest)

  

Create a new folder for the project and a virtual environment

```
mkdir <path/to/project>
```

```
cd <path/to/project>
```

Create a virtual environment

```
python3 -m venv myvenv
```

And activate it:

```
source myvenv/bin/activate
```

  

Install the package with the following command (the name may change depending on the release version):

```
pip install mfc-0.1.1-py3-none-any.whl
```

# Using the software
*You can use data in the section Sample Data below*
  

## Basic commands

### With docker installation

To caclulate the odds with the CLI on docker use the following command:

```
docker run -p 5000:5000 --rm -v '<absolute/path/to/local/empire.json>':/data/empire.json  raymond93/millenium-falcon-challenge-back mfc solve millennium-falcon.json empire.json
```
You can also provide millennium-falcon.json and a universe.db in a folder like so:

```
docker run -p 5000:5000 --rm -v '<absolute/path/to/folder>':/data/ raymond93/millenium-falcon-challenge-back mfc solve millennium-falcon.json empire.json
```
Make sure the files are named correctly (millennium-falcon.json, empire.json, universe.db)

To start the local web server, you can execute
```
docker run -p 5000:5000 --rm -v '<absolute/path/to/folder>':/data/ raymond93/millenium-falcon-challenge-back mfc serve millennium-falcon.json
```
Make sure you include the files named correctly (millennium-falcon.json and universe.db)

### With host installation
  

To caclulate the odds with the CLI use the following command:

  

```
mfc solve path/to/millennium-falcon.json path/to/empire.json
```

Make sure that the universe.db in the millennium-falcon.json exists and is correct.

  

To launch the local web server :

```
mfc serve path/to/millennium-falcon.json
```

This will create a basic web server to calculate the odds via a web interface.

  

You can also use the following command if you need help:

  

```
mfc --help
```


## Sample data

You can use the following sample data to test the app

  

[universe.db](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/universe.db?raw=true)

  

[millennium-falcon.json](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/millennium-falcon.json?raw=true)

  

[empire.json](https://github.com/dataiku/millenium-falcon-challenge/blob/master/examples/example2/empire.json?raw=true)

# What can be improved?
1. Put a cache in the odds calculation function 
2. Create a CI using type checkers, unit tests...
3. Add docstrings
4. Improve the algorithm by optimizing the planets and paths. Precalculate the paths with the database and load them once
5. The database is loaded in memory but if it is big, the app should be able to query the database directly. We could also add asynchronous programming in this case
6. Manage big empire.json file
7. Show more detail in validation error when loading the files on the server
8. For production, create a real architecture for the server (with Gunicorn) 
9. Enable host port customization
10. Improve the UI/UX on the frontend
