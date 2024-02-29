# Reverse shell

A ground-laying project to discover how setting up a reverse shell works, and what it does.

## And How does it ?

The server awaits for a drone to connect to it, before sending it commands.
Obviously, for this to work the drone has to be sneaked onto the targeted device, and remotely activated.

## Setup

### Necessary tech
On both the server and the target:
- Python 3
- socket library

### Config

On both script "HOST" and "PORT" need to be configured with the IP and the port of the server that are going to be used in this process.



Next :  
-> Scan the device to see if there's juicy stuff.  
-> Scan the network for the same reason.  
-> Hide the drone.  
-> Make it persistent.  
-> Give it the ability to spread ?  
-> Profit.  
-> Flee to another planet.  
