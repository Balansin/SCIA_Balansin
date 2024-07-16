import uuid
import sys
import clr
import os
from pathlib import Path
import sys

print(sys.version)
print(uuid.uuid4())  # Generate UUID
print(Path.cwd())    # pathlib


print("Current working directory: ", os.getcwd())
os.chdir(r"C:\Program Files\SCIA\Engineer24.0\OpenAPI_dll")
print("New working directory: ", os.getcwd())

sys.path.append(r"C:\Program Files\SCIA\Engineer24.0\OpenAPI_dll")

clr.AddReference(r"C:\Program Files\SCIA\Engineer24.0\OpenAPI_dll\SCIA.OpenAPI.dll")
clr.AddReference(r"C:\Program Files\SCIA\Engineer24.0\OpenAPI_dll\EnvESA80.dll")


from SCIA.OpenAPI import *
from SCIA.OpenAPI.StructureModelDefinition import *
from SCIA.OpenAPI.Results import *
from Results64Enums import *
from envesa80 import *
from system import guid

