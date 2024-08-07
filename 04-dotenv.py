password = "my_password" # don't do this

# do the below instead
# usually at the top with your imports

import os # comes with python
from dotenv import load_dotenv # something you install

load_dotenv()

os.getenv("PASSWORD") # use this line instead of your actuall password
password = os.getenv("PASSWORD")
