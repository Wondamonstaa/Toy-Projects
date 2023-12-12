import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.net.Socket;
import java.util.function.Consumer;



public class Client extends Thread{


    Socket socketClient;
    int clientPort;
    int playerID = 0;
    String ipAddr;
    GameInfo data = new GameInfo();

    ObjectOutputStream out;
    ObjectInputStream in;

    private Consumer<GameInfo> callback;

    Client(Consumer<GameInfo> call, String ip, int port){

        callback = call;
        ipAddr = ip;
        clientPort = port;
    }

    public void run() {

        try {
            socketClient= new Socket(ipAddr,clientPort);
            out = new ObjectOutputStream(socketClient.getOutputStream());
            in = new ObjectInputStream(socketClient.getInputStream());
            socketClient.setTcpNoDelay(true);
            System.out.println("Connected.");
        }
        catch(Exception e) {
            System.out.println("Failed to connect");
        }

        try {
            out.writeObject(data);
            System.out.println("\nSyncing game board.\n");
        }
        catch (Exception e) {
            System.out.println("Error writing built board.");
        }

        while(true) {

            try {

                data = (GameInfo) in.readObject();
                if (data.playerID == -1) {
                    callback.accept(data);
                    System.out.println("Disconnecting...");
                    break;
                }
                callback.accept(data);
            }
            catch(Exception e) {
                System.out.println("Unable to receive data.");
                break;
            }
        }

    }

    public void send(GameInfo data) {

        try {
            out.writeObject(data);
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }


}