from sqlalchemy import (create_engine, Table, Column, MetaData, 
                        Integer,  String, inspect)
from infra.infra import databasePath 

class subsets:

    def __init__(self) -> None:        
        self.table_name = 'subsets'
        self.database_path = databasePath()

    def update(self):
        engine = create_engine(f'sqlite:///{self.database_path}')  # Access the DB Engine
        if not inspect(engine).has_table(self.table_name):  # If table don't exist, Create.
            
            metadata = MetaData(engine) 
            Table(
                self.table_name, 
                metadata,
                Column('id', Integer, primary_key=True, nullable=False , autoincrement=True), 
                Column('subset', String)
            )
            # Implement the creation
            metadata.create_all()  
