# flask-sqlalchemy-templates

Commands:
Run the container to start the db:
**docker run -d -p 3306:3306 --name mysql_container -e MYSQL_ROOT_PASSWORD=test mysql**
**docker inspect mysql_container | grep IPAddress**
**mysql -h <mysql_container_ip> -P 3306 -u root -p<db_password> -e "CREATE DATABASE crud_db;"**

Start the virtual environment:
**source venv/bin/activate**

Deactivate the virtual environment:
**deactivate**