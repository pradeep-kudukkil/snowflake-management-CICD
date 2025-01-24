import snowflake.connector
import os

# Get the environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
print(db_username)
print(db_password)
# Connect to Snowflake
connection = snowflake.connector.connect(
    user=db_username,
    password=db_password,
    account='zsbuhwf-bp99278', 
    database='PRADEEP_TEST',
    schema='MIGRATIONS', 
    warehouse='COMPUTE_WH', 
    role='ACCOUNTADMIN' 
)

# Create a cursor object
cursor = connection.cursor()

try:
    # Execute a query
    create_table_query = """
        CREATE TABLE employees (
        employee_id INT PRIMARY KEY,        
        first_name STRING,                   
        last_name STRING
    );
    """
    cursor.execute(create_table_query)
    print("Table created")
    

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
