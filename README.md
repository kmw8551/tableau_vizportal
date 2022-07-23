<div align="center">
  <img src="https://cdn.worldvectorlogo.com/logos/tableau-logo.svg"><br>
</div>

# Tableau VizPortal - Unofficial Python3 Library
-----------------------------------
[![License](https://img.shields.io/github/license/kmw8551/tableau_vizportal)](https://github.com/kmw8551/tableau_vizportal/blob/master/LICENSE)
[![](https://tokei.rs/b1/github.com/kmw8551/tableau_vizportal)](https://github.com/kmw8551/tableau_vizportal)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-3776AB?logo=Python&logoColor=FFFFFF&style=flat-square)](https://www.python.org/)
[![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=kmw8551.tableau_vizportal&color=1D70B8&logo=GitHub&logoColor=FFFFFF&style=flat-square)](https://github.com/kmw8551/tableau_vizportal)

## Author

- Min Woong, Kang 


## What is VizPortal ?

<div align="center">
  <figure>
  <img src="https://ittutorial.org/wp-content/uploads/2020/05/2-Architecture.png"><br>
  <figcaption>
   Fig 1. https://ittutorial.org/tableau-server-architecture/
  </figcaption>
  </figure>
</div>  
  

Follow this Link : [Tableau Vizportal](https://help.tableau.com/current/server/en-us/server_process_application-server.htm)  
Tableau Vizportal : Application Server (VizPortal) handles the web application and REST API calls  

  
## Purpose of this Repo - What's the Difference???
In this Repo, I added "Data Alert" Part. For those looking for an additional api methods, please refer to the link below for more details  
[other API Methods](https://viziblydiffrnt.github.io/blog/2017/01/26/documenting-tableau-vizportal-api)

---  
## Usage

examples.py -> Check this Py file!


### Explanation  
To Understand this lib, The First thing you need to know is, "Login Flow"  
<br>
Tableau Login Flow(both Web UI and API)  
<br>
**[Web]**  
<span style='background-color: #dcffe4'>Login -> Select site -> Home</span>    

**[API]**  :arrow_right: Our Process  
<span style='background-color: #dcffe4'>Get PublicKey -> Encrypt password -> Login to Server using publick key ID and encrypted password</span> -> <span style='background-color: #ffdce0'>using SwitchSite API to switch site, else move to 'Default'</span>   

<br>
This Lib has 2 major parts : Authentication and API Factory  

Here, "Endpoint" Class is the base class, and all APIs inherit "Endpoint" class





