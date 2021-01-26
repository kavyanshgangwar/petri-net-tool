# Description of the CLI functions.

Different Classes:
* ## Places
   - __Get_tokens__  --> Returns the no of tokens for particular Place.
   - __add_tokens__ --> add  particular value to the number of tokens.
   - __hasatleast__ --> returns boolean value whether current Place has minimum no of tokens.
* ## Transitions
  - __add_arc__ --> adds arc to incoming arcs list/ outgoing arcs list based on its type.
  - __can_fire__ --> checks for the condition whether a transition can be fired or not.
  - __fire__ --> changes all possible Place tokens associated with current transition.
* ## Arcs
  - Nothing Special.
