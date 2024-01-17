#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'bfs' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 *  3. 2D_INTEGER_ARRAY edges
 *  4. INTEGER s => we start traversal from s
 */

vector<int> bfs(int n, int m, vector<vector<int>> edges, int s) {
    
    //Initialize the visited array with the size of n+1, and all elements to false
    vector<bool> visited(n + 1, false);
    
    //Init the distances array of size n with all elements to -1
    vector<int> distances(n, -1);
    
    //The queue for BFS algorithm
    list<int> q;

    //The first node is guaranteed to be visited, since we start from it. So, mark it as visited
    visited[s] = true;
    
    //Update the distances storage
    distances[s - 1] = 0;
    
    //And populate the queue with the starting node
    q.push_back(s);

    while (!q.empty()) {
        
        //The first node in the queue
        int current = q.front();
        
        //Clear it
        q.pop_front();

        for (const auto &edge : edges) {
            
            int u = edge[0];
            int v = edge[1];

            if (u == current && !visited[v]) {
                visited[v] = true;
                distances[v - 1] = distances[current - 1] + 6;
                q.push_back(v);
            } else if (v == current && !visited[u]) {
                visited[u] = true;
                distances[u - 1] = distances[current - 1] + 6;
                q.push_back(u);
            }
        }
    }
    
    for(vector<int> :: iterator it = distances.begin(); it != distances.end(); ++it){
        if(*it == 0){
            distances.erase(it);
        }
    }

    return distances;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int n = stoi(first_multiple_input[0]);

        int m = stoi(first_multiple_input[1]);

        vector<vector<int>> edges(m);

        for (int i = 0; i < m; i++) {
            edges[i].resize(2);

            string edges_row_temp_temp;
            getline(cin, edges_row_temp_temp);

            vector<string> edges_row_temp = split(rtrim(edges_row_temp_temp));

            for (int j = 0; j < 2; j++) {
                int edges_row_item = stoi(edges_row_temp[j]);

                edges[i][j] = edges_row_item;
            }
        }

        string s_temp;
        getline(cin, s_temp);

        int s = stoi(ltrim(rtrim(s_temp)));

        vector<int> result = bfs(n, m, edges, s);

        for (size_t i = 0; i < result.size(); i++) {
            fout << result[i];

            if (i != result.size() - 1) {
                fout << " ";
            }
        }

        fout << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
