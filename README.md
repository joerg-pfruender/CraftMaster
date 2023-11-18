# Welcome to CraftMaster 

This is a fork of https://github.com/RexWangSida/CraftMaster adapted for learning python.

## Table of Content
- [**What is CraftMaster?**](#what)
- [**Where to start?**](#where)
- [**CraftMaster Views**](#views)
- [**Open Issues**](#open)


## <a name = "what"> What is CraftMaster❓</a>

CraftMaster is a 3D sandbox game developed by three software engineering students at Mcmaster University. It is a reimplementation of [@fogleman/Minecraft](https://github.com/fogleman/Minecraft)(refered to as orginal project) which is developed by **_Michael Fogleman_**. CraftMaster is written in [**Python**](https://www.python.org/) with [**Pyglet**](http://pyglet.org/). All the media source are open-source and found online.

<div align = "center"><img src="./CraftMasterGame/src/source/icon.png" width="50%" height="50%"></div>

## <a name = "where">Where to start❓</a>

### Requirements

| Software        | [Chocolatey](https://chocolatey.org/) (Windows) | Ubuntu Linux                                    | [Homebrew](https://brew.sh/)     | URL                                                                                                                            |
|-----------------|-------------------------------------------------|-------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Git**         | `choco install git`                             | `sudo apt install git`                          | `brew install git`               | [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) |
| **Python**(3.8) | `choco install python38`                        | built in                                        | `brew install python@3.8`        | [https://www.python.org/downloads/]                                                                                            |
| **PyCharm**     | `choco install pycharm-community`               | `sudo snap install pycharm-community --classic` | `brew install --cask pycharm-ce` | [https://www.jetbrains.com/edu-products/download/#section=pycharm-edu]                                                         |

### Installation

#### 1.clone repository

git clone https://github.com/joerg-pfruender/CraftMaster


create virtual environment:
https://realpython.com/python-virtual-environments-a-primer/

*nix: `python3 -m venv venv`

Windows `python -m venv venv`




```shell
pip install python
```
- To install **pyglet**(it requires pip to be installed), run:
```shell
pip install pyglet==1.5.27
```
- To start the program, sequentially run:

```shell
cd CraftMaster/CraftMasterGame/src
```
```shell
python main.py
```
- To learn the instruction of how to play the game, follow the [**CraftMaster User Guide**](https://github.com/RexWangSida/CraftMaster/blob/master/CraftMasterGame/Docs/UserGuide/UserGuide.pdf).

## <a name = "views"> CraftMaster Views🏔</a>

<div align = "center"><img src="./CraftMasterGame/Views/view4.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view1.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view2.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view3.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view5.png" width="50%" height="50%"></div>


## <a name = "ac"> Special Thanks 🎉</a>
We gratefully thank **_Thien Trandinh_** for the guidance throughout the term and **_Michael Fogleman_** for giving us permissions to modify the amazing original project and allow us to develop CraftMaster on the base of it.

