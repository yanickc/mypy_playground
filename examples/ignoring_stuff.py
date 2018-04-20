

from Crypto import Random


Random.get_random_bytes(5) # type: ignore
# or that would work
#Random.new().get_random_bytes(5)

# Without the ignore, we get:  error: Module has no attribute "get_random_bytes"
# Due to the way the Random module declares its exports