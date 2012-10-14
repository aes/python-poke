
poke - Peek and poke for CPython
................................

license
-------

Poke uses the Artistic License.

API
---

.. module:: poke

.. function:: peek(address, length) -> string
   Read length bytes from address.

.. function:: poke(address, string) -> None
   Write string to the address.
