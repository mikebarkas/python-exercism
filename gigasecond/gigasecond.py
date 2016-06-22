from datetime import timedelta

# Gigasecond - when someone will celebrate their 1 Gs anniversary.
def add_gigasecond(birthday):
    return birthday + timedelta(seconds=(10**9)) 

