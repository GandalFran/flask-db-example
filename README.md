# flask-sql-example

### How to deploy

1. Install mariadb with `apt install mariadb-client mariadb-server -y`
2. Prepare database with the script that you will find in sql_script/createDB.sql: `sudo mysql < createDB.sql`
3. Install mysql library for mysql-python-connector library `sudo apt-get install libmariadbclient-dev`
4. Install setuptools `pip3 install setuptools`
5. Install python-flask server requeriments with `python3 setup.py install`
6. Run server with `python3 run.py`

### Try it out
Go to http://localhost:8080/, and see the swagger doc to know more about available endpoints.
FYI: if you don't know swagger, you cant try registereda API endpoints in it.
