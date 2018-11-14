#Stack machine has 2 types in it:
# points on elliptic curve
# bytes

#There are implicit casts:
# bytes -> numbers (big endian)
# numbers -> bytes (big endian)
# bytes -> bools (nonzero bytes -> false, anythin else ->true) 
# points -> bytes (serialization)
# bytes -> points (deserialization)
# bools -> bytes (true -> 0x01, false ->0x00)
# no chains of casts: points will not be casted to number or bool

# If there is not enough elements on stack, return false
# If there wrong type of element on stack, return false
# If note enough bytes in script for load opcode, return false
# If element on stack is not 33 bytes long or can not be casted to valid point and implicit cast is required, return False
# If 33 bytes after OP_PUSH_POINT can not be treated as valid point serialization, return false
# Any unknown opcode has "immediately return true" effect
# If execution is finished and no value was returned, cast last element to bool and return (in this specific case any valid point will be casted to true), if no elements on main stack return False

OP_RETURN = 0x00 
OP_TRUE = 0x01 
OP_FALSE = 0x02 
OP_PUSHPOINT = 0x03 
OP_PUSHBYTE = 0x04 
OP_PUSH2BYTES = 0x05 
OP_PUSH32BYTES = 0x06 

OP_PUSHBYTES = 0x07 

OP_BOOLINVERT = 0x08 

OP_IF = 0x09 
OP_ELSE = 0x0a 
OP_ENDIF = 0x0b 

OP_INITIALIZESTACKS = 0x0c 
OP_TOALTSTACK = 0x0d 
OP_FROMALTSTACK = 0x0e 

OP_DUP = 0x0f 
OP_DEPTH = 0x10 
OP_ALTDEPTH = 0x11 
OP_TYPEOF = 0x12 

OP_DROP = 0x13 
OP_SWAP = 0x14 
OP_ARBITRARYSWAP = 0x15 
OP_PICK = 0x16 
OP_ROLL = 0x17 

OP_SIZE = 0x18 

OP_EQUAL = 0x19 
OP_STRICTEQUAL = 0x1a 

OP_INCREMENT = 0x1b 
OP_DECREMENT = 0x1c 
OP_ADD = 0x1d 
OP_SUBTRACT = 0x1e 
OP_LESSTHAN = 0x1f 
OP_LESSTHANOREQUAL = 0x20 
OP_MIN = 0x21 
OP_MAX = 0x22 
OP_MULTIDROP =0x23 


OP_SHA256 = 0x24 
OP_SHA3 = 0x25 

OP_FINDEXCESS = 0x26 


OP_OUTPUTORHASH = 0x27 

OP_2BYTESOPS = 0x28 

OP_EVAL = 0x29 

OP_BNGT = 0x30 

OP_TIMEGT = 0x31 

OP_NOTHING = 0x32 


