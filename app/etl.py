from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import text
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import pandas as pd
from app.connections import DataBaseClient

# # Read and execute the SQL script from a file
# script_file = 'migration.sql'  # Replace with the path to your .sql file
# with open(script_file, 'r') as sql_file:
#     sql_script = sql_file.read()

# # Execute the SQL script
# try:
#     session.execute(text("SHOW GRANTS FOR 'mysql_user'@'%';"))
#     session.execute(text("GRANT ALL PRIVILEGES ON mysql_database.* TO 'mysql_user'@'%';"))
#     session.execute(text("FLUSH PRIVILEGES;"))
#     session.execute(text("LOAD DATA INFILE '/data/user.csv' INTO TABLE user FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"))
#     session.commit()
#     print('SQL script executed successfully.')
# except Exception as e:
#     session.rollback()
#     print(f'Error executing SQL script: {str(e)}')
# finally:
#     session.close()


data_user = pd.read_csv('data/user.csv')
data_space_attendee = pd.read_csv('data/space_attendee.csv')
data_space_session_info = pd.read_csv('data/space_session_info.csv')

mysql_client = DataBaseClient(
    user=os.getenv("MYSQL_ROOT_USER"),
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    db=os.getenv("MYSQL_DATABASE"),
    port=os.getenv("MYSQL_PORT"),
    dialect="mysql",
    driver="pymysql",
)

mysql_client.save_dataframe_to_the_database(
    data=data_user, table_name="user", schema=os.getenv("MYSQL_DATABASE"), index=False, if_exists='replace'
)
mysql_client.save_dataframe_to_the_database(
    data=data_space_attendee, table_name="space_attendee", schema=os.getenv("MYSQL_DATABASE"), index=False, if_exists='replace'
)
mysql_client.save_dataframe_to_the_database(
    data=data_space_session_info, table_name="space_session_info", schema=os.getenv("MYSQL_DATABASE"), index=False, if_exists='replace'
)