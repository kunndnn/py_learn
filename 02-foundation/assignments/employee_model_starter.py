from pydantic import BaseModel, Field #type: ignore

# crreate employee model
# Fields:
# id:int
# name:str(min 3 chars)
# department: optional str(default 'General')
# salary:float (must be >=10000)
