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

| Software         | [Chocolatey](https://chocolatey.org/) (Windows)                          | Ubuntu Linux                                    | [Homebrew](https://brew.sh/) (Mac&nbsp;OS)                               | URL                                                                                                                                          | Comment            | 
|------------------|--------------------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| **Git**          | `choco install git`                                                      | `sudo apt install git`                          | `brew install git`                                                       | [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)               |                    |
| **Python**(3.10) | `choco install python --version=3.10.0`                                  | built in                                        | `brew install python@3.10`                                               | [https://www.python.org/downloads/](https://www.python.org/downloads/)                                                                       |                    |
| a) **PyCharm**   | `choco install pycharm-community`                                        | `sudo snap install pycharm-community --classic` | `brew install --cask pycharm-ce`                                         | [https://www.jetbrains.com/edu-products/download/#section=pycharm-edu](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu) | for fast computers |
| b) **Eric**      | [Download Eric](https://eric-ide.python-projects.org/eric-download.html) | `sudo apt install eric`                         | [Download Eric](https://eric-ide.python-projects.org/eric-download.html) | [https://eric-ide.python-projects.org/](https://eric-ide.python-projects.org/)                                                               | for slow computers |

### Installation


| Step                                                                                       | Linux / Mac&nbsp;OS                                        | Windows                                                    |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| clone the repository                                                                       | `git clone https://github.com/joerg-pfruender/CraftMaster` | `git clone https://github.com/joerg-pfruender/CraftMaster` | 
| cd into the source directory                                                               | `cd CraftMaster/CraftMasterGame/src`                       | `cd CraftMaster\CraftMasterGame\src`                       | 
| [create virtual environment](https://realpython.com/python-virtual-environments-a-primer/) | `python3 -m venv venv`                                     | `python -m venv venv`                                      |
| activate virtual environment                                                               | `source venv/bin/activate`                                 | `venv\Scripts\activate`                                    | 
| install pyglet                                                                             | `pip install pyglet==1.5.27`                               | `pip install pyglet==1.5.27`                               | 
 
### Start the program

| Step                                                                                         | Linux / Mac&nbsp;OS                  | Windows (cmd)                          |
|----------------------------------------------------------------------------------------------|--------------------------------------|----------------------------------------|
| cd into the source directory                                                                 | `cd CraftMaster/CraftMasterGame/src` | `cd CraftMaster\CraftMasterGame\src`   | 
| [activate virtual environment](https://realpython.com/python-virtual-environments-a-primer/) | `source venv/bin/activate`           | `venv\Scripts\activate`                | 
| run program                                                                                  | `python main.py`                     | `python main.py`                       |   

#### troubleshooting

##### Cannot load swrast and iris drivers

**error message**

```
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: swrast
```

**fix**
* find libstdc++.so.6 on your hard disk: `sudo find / -name libstdc++.so.6`
* you might find it in `/usr/lib/i386-linux-gnu/libstdc++.so.6` or `/usr/lib/x86_64-linux-gnu/libstdc++.so.6`
* export it into LD_PRELOAD, e.g. like: `export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`

**more information**
https://stackoverflow.com/questions/71010343/cannot-load-swrast-and-iris-drivers-in-fedora-35/72200748#72200748


### How to play

To learn the instruction of how to play the game, follow the [**CraftMaster User Guide**](https://github.com/RexWangSida/CraftMaster/blob/master/CraftMasterGame/Docs/UserGuide/UserGuide.pdf).

## <a name = "views"> CraftMaster Views🏔</a>

<div align = "center"><img src="./CraftMasterGame/Views/view4.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view1.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view2.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view3.png" width="50%" height="50%"></div>
<div align = "center"><img src="./CraftMasterGame/Views/view5.png" width="50%" height="50%"></div>


## <a name = "ac"> Special Thanks 🎉</a>
We gratefully thank **_Thien Trandinh_** for the guidance throughout the term and **_Michael Fogleman_** for giving us permissions to modify the amazing original project and allow us to develop CraftMaster on the base of it.

