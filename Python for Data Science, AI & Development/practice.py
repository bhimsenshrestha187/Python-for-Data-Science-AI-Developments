import re

text = "I love cats. cats are great!"
result = re.sub(r"cats", "dogs", text)
print(result)  # Output: I love dogs. Dogs are great!