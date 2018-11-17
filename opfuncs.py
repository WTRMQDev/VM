from utils import ScriptException, ReturnException, StackData, StackBytes, StackPoint, itb
from typing import Dict, List, TYPE_CHECKING
from opcodes import *

        


# There are a lot of code
# ```
# if isinstance ...:
#   ...  
# else:
#   raise ...
# ```
# While it goes against 'Easier to ask for forgiveness than permission'
# it is the only good enough workaround for mypy testing

def f_RETURN(stacks: List[List[StackData]], script: bytes) -> bytes:
  result = stacks[0].pop()
  if isinstance(result, StackBytes):
    raise ReturnException(value = result.to_bool())
  else:
    raise ScriptException("Bool casted to %s"%type(result))
  return script

def f_FALSE(stacks: List[List[StackData]], script: bytes) -> bytes:
  stacks[0].append(StackBytes(b"\x00"))
  return script

def f_TRUE(stacks: List[List[StackData]], script: bytes) -> bytes:
  stacks[0].append(StackBytes(b"\x01"))
  return script

def f_PUSHPOINT(stacks: List[List[StackData]], script: bytes) -> bytes:
  raise NotImplementedError
  s_point, script = script[:33], script[33:]
  return script

def f_PUSHBYTE(stacks: List[List[StackData]], script: bytes) -> bytes:
  s_byte, script = script[:1], script[1:]
  stacks[0].append(StackBytes(bytes(s_byte)))
  return script

def f_PUSH2BYTES(stacks: List[List[StackData]], script: bytes) -> bytes:
  s_bytes, script = script[:2], script[2:]
  stacks[0].append(StackBytes(bytes(s_bytes)))
  return script

def f_PUSH32BYTES(stacks: List[List[StackData]], script: bytes) -> bytes:
  s_bytes, script = script[:32], script[32:]
  stacks[0].append(StackBytes(bytes(s_bytes)))
  return script


def f_PUSHBYTES(stacks: List[List[StackData]], script: bytes) -> bytes:
  _len_element = stacks[0].pop()
  if isinstance(_len_element, StackBytes):
   _len = _len_element.to_int()
  else:
    raise ScriptException("Int casted to %s"%type(_len_element))
  if _len>1023:
    raise ScriptException("PUSHBYTES argument is too long: %d"%(_len))
  s_bytes, script = script[:_len], script[_len:]
  stacks[0].append(StackBytes(bytes(s_bytes)))
  return script

def f_BOOLINVERT(stacks: List[List[StackData]], script: bytes) -> bytes:
  result = stacks[0].pop()
  if isinstance(result, StackBytes):
    res = not result.to_bool()
    sb_res = StackBytes(itb(res))
    stacks[0].append(sb_res)
  else:
    raise ScriptException("Bool casted to %s"%type(result))
  return script

def f_INITIALIZESTACKS(stacks: List[List[StackData]], script: bytes) -> bytes:
  number_of_stacks = stacks[0].pop()
  if isinstance(number_of_stacks, StackBytes):
    number_of_stacks_int=number_of_stacks.to_int()
  else:
    raise ScriptException("Int casted to %s"%type(number_of_stacks))
  if number_of_stacks_int+len(stacks)>255:
    raise ScriptException("To much stacks: current %d, to activate %d"%(len(stacks), number_of_stacks_int))
  for i in range(number_of_stacks_int):
    stacks.append([])
  return script

def f_TOALTSTACK(stacks: List[List[StackData]], script: bytes) -> bytes:
  stack_index = stacks[0].pop()
  element = stacks[0].pop()
  if isinstance(stack_index, StackBytes):
    stack_index_int=stack_index.to_int()
  else:
    raise ScriptException("Int casted to %s"%type(stack_index))
  if stack_index_int>len(stacks)-1:
    raise ScriptException("Operation with inactivated stack %d"%(stack_index_int))
  stacks[stack_index_int].append(element)
  return script

def f_FROMALTSTACK(stacks: List[List[StackData]], script: bytes) -> bytes:
  stack_index = stacks[0].pop()
  if isinstance(stack_index, StackBytes):
    stack_index_int=stack_index.to_int()
  else:
    raise ScriptException("Int casted to %s"%type(stack_index))
  if stack_index_int>len(stacks)-1:
    raise ScriptException("Operation with unactivated stack %d"%(stack_index_int))
  element = stacks[stack_index_int].pop()
  stacks[0].append(element)
  return script



