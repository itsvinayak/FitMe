# FitMe


## Django

Django is an open-source python web framework used for rapid development, pragmatic, maintainable, clean design, and secures websites. A web application framework is a toolkit of all components need for application development. The main goal of the Django framework is to allow developers to focus on components of the application that are new instead of spending time on already developed components. Django is fully featured than many other frameworks on the market. It takes care of a lot of hassle involved in the web development; enables users to focus on developing components needed for their application.



[![Made with python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://github.com/itsvinayak/fitme)

<img src="screenfit.png"/>


## Virtualenv & Dependencies

create a virtualenv and run requirements.txt<br/>
<b>virtualenv</b>

<pre>pip install virtualenv</pre>

<b> what is virtual environment ? </b><br/>
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.
<br/>
<a href="https://www.geeksforgeeks.org/python-virtual-environment/" >read more... </a>

to run requirements.txt

<pre>$ pip install -r requirements.txt</pre>
 
here <b>env/</b> folder contains all dependencies


## Running locally

<ol>
  <li>
      clone repository 
      <pre>$ git clone https://github.com/itsvinayak/fitme.git</pre>
  </li>
  <li> 
     install virtual environment
     <pre>pip install virtualenv</pre>
 </li>
  <li>
    make and activate virtual env
   <pre>virtualenv env1</pre>
   <pre>env1\Scripts\activate</pre>
   <pre>pip install -r requirements.txt</pre>
  <li>
     make database settings and connect it to your local database(if you want to use mysql else skip this step) 
    <pre>$ cd ./src/FitMe </pre>
    open <b>settings.py</b> file
    <pre>
                DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "iert",
                "USER": "root",
                "HOST": "localhost",
                "PASSWORD": "vinayak",
                "PORT": "3306",
                "OPTIONS": {"sql_mode": "traditional"},
            }
        }
   </pre>
   set this part according to needs.
  </li>
 <li> in src dir </li>
  <li>
    run migrations 
    <pre>$ python manage.py migrate</pre>
  </li>
  <li>
    to create admin 
   <pre>$ python3 manage.py createsuperuser</pre>
  <li>
    now, runserver 
    <pre>$ python manage.py runserver</pre>
  </li>
 
 </ol>




## Features

<ul>
  <li>responsive bootstrap design </li>
  <li>Trainee and Trainer login and registration feature</li>
  <li>Task assignment and update </li>
  <li>dashboard with graphs and animations</li>
</ul>



## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/itsvinayak/fitme 
