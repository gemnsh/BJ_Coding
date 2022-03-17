import java.util.Scanner;

public class Main {

    private static boolean checkIfConnected(int numberOfSites, int[][] connections) {

        /* Your program should set the following variable to true if the graph formed
         * by the specified onnections is connected, i.e., there is a path from every 
         * site to every other site. */
        boolean isConnected = false;

        /* ------------------- INSERT CODE HERE ---------------------*/
boolean[] visited = new boolean[numberOfSites];
        for(int i = 0; i < visited.length; i++) 
            visited[i] = false;

        visited[0] = true;

        boolean nochange;

        do {
            nochange = true;

            for(int i = 0; i < connections.length; i++) {
                if(visited[connections[i][0]] && !visited[connections[i][1]]) {
                    visited[connections[i][1]] = true;
                    nochange = false;
                } else {
                    if(visited[connections[i][1]] && !visited[connections[i][0]]) {
                        visited[connections[i][0]] = true;
                        nochange = false;
                    }
                }
            }

        } while(nochange == false);

        isConnected = true;
        for(int i = 0; i < visited.length; i++) {
            if(! visited[i]) {
                isConnected = false;
                break;
            }
        }


        /* -------------------- END OF INSERTION --------------------*/

        return isConnected;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numCases = sc.nextInt();

        for(int i = 0; i < numCases; i++)
        {
            int numberOfSites = sc.nextInt();
            int numberOfConnections = sc.nextInt();

            int[][] connections = new int[numberOfConnections][2];

            for(int j = 0; j < numberOfConnections; j++) {
                connections[j][0] = sc.nextInt();
                connections[j][1] = sc.nextInt();
                assert(connections[j][0] < numberOfSites);
                assert(connections[j][1] < numberOfSites);
            }

            if(checkIfConnected(numberOfSites, connections)) {
                System.out.println("Connected.");
            } else {
                System.out.println("Not connected.");
            }
        }
    }
}
