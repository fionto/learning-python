from pathlib import Path

# 1. The actual system home directory
system_home = Path.home()

# 2. A relative folder named 'home'
literal_home = Path('home')

print(f"System Home: {system_home}")
print(f"Literal 'home': {literal_home}")
print(f"Is 'home' inside System Home? {literal_home.is_relative_to(system_home)}") 