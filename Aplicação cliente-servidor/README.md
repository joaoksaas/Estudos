<h1 align="center">
  rock-paper-scissors
</h1>

## This is a simple implementation of the game rock paper scissor using client-server application.

This project was created for studying purposes with the objective of learn client-server application using sockets library in python.

### How does it work?
The implementation of the architecture was done using 4 components for simulating the game of rock, paper, and scissors. The involved components are 2 servers: server 1 and 2, and 2 clients: client 1 and 2.
The idea is simple, server 1 is connected to server 2 through file communication, and it is also connected to clients 1 and 2 with sockets. 
The server sends the request for the choice in the game (rock, paper, or scissors) to the clients. After receiving the choices from both clients, it sends them to server 2,
which performs the logical processing to decide the winner. Server 2, after determining the winner, returns the message to server 1, which, in turn, returns it to the clients.
