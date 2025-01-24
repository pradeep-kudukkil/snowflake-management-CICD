import snowflake.connector

# Connect to Snowflake
connection = snowflake.connector.connect(
    user='PRADEEPKUDUKKIL',
    password='Test@7376@',
    account='zsbuhwf-bp99278',  # e.g., xy12345.us-east-1
    database='PRADEEP_TEST',
    schema='MIGRATIONS',  # Optional
    warehouse='COMPUTE_WH',  # Optional
    role='ACCOUNTADMIN'  # Optional
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
