# Bcpy-manager
It's just a python package manager

linux is the only os that supports this package manager for now.

## Installation
```
$ git clone https://github.com/bcbro2021/bcpy-package-manager.git
$ cd bcpy-package-manager
$ ./setup.sh
```

## Usage
```
$ bcpy <function> <package-name> <directory>

```
### Functions
```
  install :- installs a package from <directory>
  remove :- removes a package from <directory>
```
### Directory
```
  example: $bcpy install margray_2d /home/<your-username>/projects/python/game/
  
  or
  
  example: $bcpy install margray_2d global (global :- saves to the default python package directory)
  
```
