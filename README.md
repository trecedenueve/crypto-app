# crypto-app
Project to see the value of the main cryptocurrencies by making requests to an api throughout the day. 

## Considerations:

### 1 . Virtual enviorenment 
In the linux machine it is advisable to create a virtual environment, if we do not have it. It is assumed that we have python3 installed.
    - sudo apt install python3-venv
    - python3 -m venv my_environment

### 2. preparing the archives
    In the user's folder a new folder called “python” has been created. /home/user/python/

### 3. Bash script
    We will create a script so that the file “crypto.py” is executed automatically, “ejecutar_crypto.sh”.

### 4. Crontab
4. We need a new task in the debian cron. We edited the crontab file and added when the script will be executed, in this case at 7, 12, 17 and 22 o´clock every day of the week.
    0 7,12,17,22 * * * ~/python/run_crypto.sh

The first time we run the script it will create a csv file, with the data of the top ten cryptocurrencies. It will also create a log file. All inside the path; /home/user/python
