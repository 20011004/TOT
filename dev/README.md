# How to do with your own stuff

**Before using the db you need to create it.**
1. Make sure you have access to a dbms like MySQL (you need a username and a password, ask to the dbms's admin).
2. Access the dbms with `mysql -u <username> -p` and insert the password when asked.
3. Type `source /path/where/you/saved/dbcreation.sql` where dbcreation.sql is the file in this directory. This will create the db structure, also with known ports.
4. Now you're ready to fill the db with informations, have fun ;)

**How to use db.py**

  Call `python2.7 db.py /complete/path/to/directory/report/` where report is the directory with subdirectories named after analyzed domains. Remember to type the last slash.
