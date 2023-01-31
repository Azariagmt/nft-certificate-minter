# 10 Academy NFT 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.


### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running in a linux environment.
Things might be slightly different if running things on windows.

Clone repo with submodules -- this will also clone the algorand sandbox together

```bash
git clone someurl -r
cd projdir
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate virtual env  
```bash
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Start algorand sandbox environment
```
cd sandbox
./sandbox up dev 
```

compile.py reads the two functions and writes them to the output files
build.sh builds our smartcontracts