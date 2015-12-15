# BeMyTranny
Be my translator



1. clone the whole repo
2. Inside the folder, activate the virtualenvironment. 
DO: $ source web/venv/bin/activate

You will vidn (venv) before the line

Then:

pip install flask

pip install flask-mysqldb
//Installed flask, flask-mysqldb

Then: install mySQL, start it with root user
(If you can't start mySQL, do the following:
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/


export PATH=$PATH:/usr/local/mysql/bin/


export PATH=${PATH}:/usr/local/mysql/bin
)

run the sql file in the sql folder

In the venv, do:

$brew install tesseract

//this is for classifier

Finally, do:
$python web/app.py

If you have any problem running it, contact: riyagwj@umich.edu
