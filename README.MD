# Leer VM

Leer Virtual Machine is non-Turing complete stack machine inspired by Bitcoin Script.

This stack machine has 2 types in it:
 * bytes
 * points on elliptic curve

## TODO

* Operations for points (+, multiplication)
* PUSHPOINT (patch for libsecp256k1 is required)
* Logic for `excess_lookup`, `output_lookup` and `burden` is required (stubs for now)
* tests

