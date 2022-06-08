#!/usr/bin/python3
def simple_delete(a_dictionary, key=""): 
  new = dict(a_dictionary)
  for key, val in new.items(): 
    val *= 2
    new[key] = val
  return new
