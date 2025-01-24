import snowflake.connector

# Connect to Snowflake
connection = snowflake.connector.connect(
    user='username',
    password='password',
    account='zsbuhwf-bp99278',  # e.g., xy12345.us-east-1
    database='db_name',
    schema='MIGRATIONS',  # Optional
    warehouse='COMPUTE_WH',  # Optional
    role='ACCOUNTADMIN'  # Optional
)

# Create a cursor object
cursor = connection.cursor()

try:
    delete_table_query = "DROP TABLE IF EXISTS employees;"
    cursor.execute(delete_table_query)
    print("The 'employee' table has been deleted successfully.")
    

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
