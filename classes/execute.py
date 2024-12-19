from .connect import connect
from .config import load_config

def set_table():
    conn = None
    cur = None
    try:
        # Load the configuration
        config = load_config()
        
        # Establish connection
        conn = connect(config)

        # Create a cursor object using the connection
        cur = conn.cursor()

        #drop table if exists
        drop_script="DROP TABLE IF EXISTS job_posting;"
        cur.execute(drop_script)

        # Create table if not exists
        create_script = '''CREATE TABLE IF NOT EXISTS job_posting (
            id SERIAL PRIMARY KEY,            
            job_title VARCHAR(255) NOT NULL,   
            job_link TEXT NOT NULL,           
            company_name VARCHAR(255)  
        );'''
        
        cur.execute(create_script)
        conn.commit()

    except Exception as error:
        print(f"Error: {error}")
    finally:
        # Close resources safely
        if cur:
            cur.close()
        if conn:
            conn.close()

def insert_data(insert_values):
    conn = None
    cur = None
    try:
        # Load the configuration
        config = load_config()
        
        # Establish connection
        conn = connect(config)

        # Create a cursor object using the connection
        cur = conn.cursor()
    
    # Insert script
        insert_script = '''INSERT INTO job_posting (job_title, job_link, company_name) 
                           VALUES (%s, %s, %s);'''

        # Insert data into the table
        cur.execute(insert_script, insert_values)
        conn.commit()
        print("Job posting inserted successfully.")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        # Close resources safely
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_data():
    conn = None
    cur = None
    try:
        # Load the configuration
        config = load_config()
        
        # Establish connection
        conn = connect(config)

        # Create a cursor object using the connection
        cur = conn.cursor()

        #get script
        get_script = '''SELECT * FROM job_posting;'''
        cur.execute(get_script)
        data = cur.fetchall()
        print("Job posting retrieved successfully.")
        return data
    except Exception as e:
        print(e)    
    finally:
        # Close resources safely
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

