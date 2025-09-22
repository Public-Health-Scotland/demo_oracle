This repo will allow you to connect to a database at PHS using VSCode. 

- Oracle is used for databases such as SMRA. Oracle connection requires oracledb package
- PostgreSQL is used for databases such as DENODO. PostgreSQL requires psycopg package

Clone this repo in order to have the required files in your VSCode environment.

🔴**Caution**: *Do not store your credentials in plain text or as part of your code (hardcoded).*

# Prepare your VScode
If you have never used VSCode, check the link under references on how to prepare it.

1. Run the bash script from the terminal (only the first time you use VSCode)
```
bash install_extensions.sh
```
# Prepare your Python environemnt (Python 3.12.6) (for other Python versions check reference link)
1. Create your environment (only the first time you create the project). To create an environment called .oenv, run:
```
/opt/python/3.12.6/bin/python3.12 -m venv .oenv
```
2. Activate this environment using this command in terminal (each time you open your project)
```
source .oenv/bin/activate
```
 Make sure your env name appears at the start of the line in the terminal. ![icon](img_tuto/image-2.png)

3. Update your pip (only the first time you create your environment)
```
pip install --upgrade pip wheel
```
4. Install required packages (only the first time you create your environment)
```
pip install -r requirements.txt
```

5. Create a .env file (environment variables) using vscode icon create files at the top of the list of folders: ![icon](img_tuto/image.png) 

6. You need to copy your username, password and DSN into the .env file.

Note: for SMRA, the DSN URL is something like SMRA.xxx.xxxx.xxx.xx
You can find the DSN URL by connecting to the database on R and checking the SVC variable under Connections: 
![dsn url](img_tuto/image-1.png)

```
ORACLE_USER=your_user_name
ORACLE_PASSWORD=your_password
ORACLE_DSN=your_dns_url
```

7. This step is needed if you want to connect to Denodo - PostgreSQL. Copy this info into .env file:

```
DENODO_USER=your_user_name
DENODO_PASSWORD=your_password
DENODO_HOST=your_host
DENODO_PORT=your_port
DENODO_DBNAME=your_database_name
```

Note: You can have oracle and denodo variables in the same .env file.

8. Run this code to change the permissions in your .env file (to ensure it is readable and writeable only for you):
```
chmod 600 .env
```
8. Run a demo python script through the terminal for a quick test of pulling data from oracle (you will see a table in terminal):
```
python demo_oracle.py
```

The script my_db.py contains a Python class which facilitates the connection to Oracle and retrieves data in a pandas dataframe. Call my_oracle_object.query_to_df and set an sql statement in the sql argument to get a pandas dataframe.

9. Run a demo python script through the terminal for a quick test of pulling data from PostgreSQL. It will work if you set connection to PostgreSQL (you will see a table in terminal):
```
python demo_denodo.py
```

Note: Oracle and PostgreSQL share much of their SQL syntax; however, there are some differences.

# Advanced example
- You can find an advanced data analysis example for oracle in oracle_jupyter.ipynb

# References

For more Python/vscode info: https://github.com/Public-Health-Scotland/vscode_prep
