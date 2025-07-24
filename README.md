# Prepare your VScode
1. Run the bash script in a terminal (only the first time you use VSCode)

bash install_extensions.sh

# Your Python (Python 3.12.6)
1. Create your environment (only the first time you create the project)

/opt/python/3.12.6/bin/python3.12 -m venv .oenv

2. Activate this environment using this command in terminal (all the time you open your project. Make sure your env name appears in terminal)

source .oenv/bin/activate

3. update your pip (Only the first time you create your environment)

pip install --upgrade pip wheel

4. install required packages (Only the first time you create your environment)

pip install -r requirements.txt

5. You need to create a .env file. It will contain the following info:

```
ORACLE_USER=your_user_name
ORACLE_PASSWORD=your_password
ORACLE_DSN=your_dns_url
```

6. Run in terminal for quick test (you will see a table in terminal):
python demo.py

7. the file my_db.py contains a class which will connect to Oracle. It will be used in your jupyter notebook e.g. my_jupyter.ipynb

# References

For more Python/vscode info: https://github.com/Public-Health-Scotland/vscode_prep
