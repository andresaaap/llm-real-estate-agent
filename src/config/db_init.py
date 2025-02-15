import os
import lancedb
from src.models.model import Listing
import pandas as pd
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def initialize_db():
    # Load settings
    from .settings import get_settings
    settings = get_settings()

    # Initialize LanceDB connection
    relative_path = 'data'
    absolute_path = os.path.abspath(relative_path)
    db = lancedb.connect(absolute_path)

    # Check if the table exists
    if "listings" not in db.table_names():
        table = db.create_table("listings", schema=Listing)
        print("Table 'listings' created successfully.")
    else:
        table = db.get_table("listings")
        print("Table 'listings' already exists.")

    return table

if __name__ == "__main__":
    initialize_db()