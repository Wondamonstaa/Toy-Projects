import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.function.Consumer;

import javafx.application.Platform;
import javafx.scene.control.ListView;
/*
 * Clicker: A: I really get it    B: No idea what you are talking about
 * C: kind of following
 */

public class Server{

    int count = 1;
    int ServerPort;
    HashMap<Integer, ClientThread> clients = new HashMap<Integer, ClientThread>();
    TheServer server;
    GameInfo data;
    private Consumer<GameInfo> callback;


    Server(Consumer<GameInfo> call, int port){

        callback = call;
        data = new GameInfo();
        server = new TheServer();
        ServerPort = port;
        server.start();
    }


    public class TheServer extends Thread{

        public void run() {

            try(ServerSocket mysocket = new ServerSocket(ServerPort);){
                System.out.println("Server is waiting for a client on port " + ServerPort);
                data.gameInfo = "Server is waiting for both players...";
                callback.accept(data);

                while(true) {

                    count = clients.size() + 1;
                    ClientThread c = new ClientThread(mysocket.accept(), count);
                    if (clients.size() == 2) {
                        // refuse connection
                        System.out.println("Too many clients connected.");
                        data.gameInfo = "Cannot connect more than two players connection refused.";
                        data.playerID = -1;
                        c.start();
                        continue;
                    }
                    System.out.println("Client connected!");
                    data.gameInfo = "client has connected to server: " + "client #" + count;
                    data.playerID = count;
                    callback.accept(data);
                    clients.put(count, c);
                    c.start();

                    count++;

                }
            }//end of try
            catch(Exception e) {
                data.gameInfo = "Server socket did not launch";
                callback.accept(data);
            }
        }//end of while
    }


    class ClientThread extends Thread{


        Socket connection;
        ObjectInputStream in;
        ObjectOutputStream out;

        ClientThread(Socket s, int count){
            this.connection = s;
        }

        public void updateClients(GameInfo data) {
            for(int i = 0; i < clients.size(); i++) {
                ClientThread t = clients.get(i);
                try {
                    if (clients.size() == 2) {
                        clients.get(1).out.writeObject(data);
                        clients.get(2).out.writeObject(data);
                    } else if (clients.size() == 1) {
                        if (clients.containsKey(1)) {
                            clients.get(1).out.writeObject(data);
                        } else if (clients.containsKey(2)) {
                            clients.get(2).out.writeObject(data);
                        }
                    }
                }
                catch(Exception e) {
                    System.out.println("Could not update clients.");
                }
            }
        }

        public void run(){

            try {
                in = new ObjectInputStream(connection.getInputStream());
                out = new ObjectOutputStream(connection.getOutputStream());
                connection.setTcpNoDelay(true);
                String info = data.gameInfo;
                int playerID = data.playerID;
                data = (GameInfo) in.readObject();
                data.gameInfo = info;
                data.playerID = playerID;
            }
            catch(Exception e) {
                System.out.println("Streams not open");
            }

            updateClients(data);

            while(true) {
                try {
                    data = (GameInfo) in.readObject();
                    callback.accept(data);
                    updateClients(data);

                }
                catch(Exception e) {
                    data.gameInfo = "Player " + count + " disconnecting.";
                    clients.remove(1);
                    System.out.println(e.getMessage());
                    callback.accept(data);
                    updateClients(data);
                    count--;
                    break;
                }
            }
        }//end of run


    }//end of client thread
}

