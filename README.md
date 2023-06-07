<h1 align="center">
  <a name="logo" href="https://www.cross-architecture.net/"><img src="https://images.squarespace-cdn.com/content/v1/56e80c843c44d8db592aefe7/1462354916694-9R8CINAOMEZV6UUIT9Y6/Cross-Logo-with_border-transparent-black-01.png?format=1500w" alt="Cross Architecture" width="200"></a>
  <br>
  Cross Architecture <br>
  Cross-Tools by Erich Domme
</h1>

<div align="center"></div>

<p><font size="3">
The purpose of this repository is to document all "Cross-Tools", how they work, the idea behind them and how they were implemented! The project was developed during an internship at Cross Architecture Aachen as part of the Master in Construction and Robotics at RWTH Aachen University. The aim was to implement a set of tools that the entire Cross Architecture team could use to simplify and in many cases automate repetitive, tedious and complicated tasks in their daily work with Revit. These quality of life tools were constantly tested and adapted to the working conditions. </p>

<!-- LINKS -->

<div align="center"><a name="menu"></a>
  <h4>
    <a href="https://www.pinterest.de/cross_architecture/">
      Pinterest
    </a>
    <span> | </span>
    <a href="https://www.facebook.com/CROSSArchitecture/">
      Facebook
    </a>
    <span> | </span>
    <a href="https://www.linkedin.com/company/cross-architecture/mycompany/">
      LinkedIn
    </a>
    <span> | </span>
    <a href="https://www.instagram.com/cross_architecture/">
      Instagram
    </a>
    <span> | </span>
    <a href="https://www.cross-architecture.net/">
      Homepage
    </a>
  </h4>
</div>

## Table of Contents
* [General Info](#general-information)
* [Requirements](#requirements)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->

## General Information
Cross-Tools is a collection of tools based on Dynamo and/or Python. The aim of these tools is to make your daily work with Revit easier. During the course of a building project, our architects are faced with a number of tasks that need to be completed. These tasks can often be repetitive and time consuming. That's why Cross Tools are designed to help with automation and management tasks. This includes facilitating the creation of plan sheets as well as alert management in the model. Under [Features](#features) all tools are listed and described in their use case.


## Requirements
> It is assumed that you have Autodesk Revit installed on your computer!<br>
> Revit 2021 has been used for development.

In order for Cross-Tools to run on your computer, you will need to do a few installations beforehand. Cross-Tools is based on pyRevit and this is where we start.
1. Make sure you have Autodesk Revit installed on your computer!
2. Install the latest [pyRevit version](https://github.com/eirannejad/pyRevit/releases), during the development of Cross-Tools the version [v4.8.12.22247](https://github.com/eirannejad/pyRevit/releases/tag/v4.8.12.22247%2B0031) was used. The installation is self-explanatory and very well documented, but a look at the [Notion Page](https://pyrevitlabs.notion.site/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0) is worthwhile.
3. 

## Features
* Dynamo
  * Beam(s) through input Surface
  * Excel Export
  * Delete selected unplaced Views
  * Warning Management
  * Reset Graphical Override
* Python
  * Center Room Tag
  * Same category as selected
  * same type as selected
  * Titleblocks on sheets
  * Select only categories
  * Select only 3D
  * Select only 2D
  * Deselect grouped elements


## Screenshots
<p align="center">
  <img src="./img/Toolbar.PNG" />
</p>
<!-- If you have screenshots you'd like to share, include them here. -->

## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Without these people and their projects, Cross-Tools would not have been possible:
- [Ehsan Iran-Nejad](https://github.com/eirannejad) with [pyRevit](https://github.com/eirannejad/pyRevit)
- [Erik Frits](https://github.com/ErikFrits) with [EF-Tools](https://github.com/ErikFrits/EF-Tools)
- [Gavin Crump, aussieBIMguru](https://github.com/aussieBIMguru) with [guRoo](https://github.com/aussieBIMguru/guRoo/tree/main/guRoo.tab/Tools.panel)
- [Marc Anton Dahmen](https://github.com/marcantondahmen) with [revitron](https://github.com/revitron/revitron)


## Contact
Created by [@Erich Domme](mailto:erich.domme@rwth-aachen.de) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->