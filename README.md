# HeartDiseasePredictionWebsite

This a website to predict whether a person suffers from a heart diease or not. This is a machine learning project where the prediction is made by a machine learning algorithm. The Jupyter Notebook used has been provided. The dataset was taken from Kaggle. The dataset was analyzed before passing it onto various models. Finally RandomForest was selected among various different alogorithms and then the notebook was pickled to make it run on a webserver.


## Built With
* [Django](https://www.djangoproject.com/) - The Web Framework used for backend
* [MySQL](https://www.mysql.com/) - The database used for storing data.



## Installation
After cloning or downloading this github repo on the local system. 
Create a Virual Environment on the Desktop.
```bash
virtualenv VirtualEnvironmentName
```
Now copy the repository inside your virtual environment.
Activate the virtual environment.
```bash
~/desktop/VirtualEnvironmentName/Scripts/activate
```
Move inside the virtual environment.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
```bash
pip install -r requirements.txt
```
Or 
Install the following to run on local host.
```bash
pip install django
pip install Pillow
```
Change directory to blogs.
Run the following command
```bash
python manage.py runserver
```
An IP address will be shown, copy it and run it on a web browser.

## Using the app
Internet connection is a must to run the app.

The app is now live at localhost.


