# sigon

Sigon is a framework for the development of agents as multi-context systems.
It is a generic and extensible tool that allows modeling agents according to existing architectures or to create new ones, as well as to extend an agent construction with additional features through other contexts and bridge rules.

## Installation


```
pip install -r requirements.txt
```


## Implementation details

Each sensor is responsible for defining how each data can be used during the reasoning cycle. A sensor's implementation must:
1. Define how data is transformed to perception (add method);
2. How the perception can be verified during bridge-rules execution (verify method).

## Contributing 


### With development

1. Creating a fork from master
2. Making and Submitting Changes
3. Submit a pull request to the repository

### With ideas

1. Creating an issue

