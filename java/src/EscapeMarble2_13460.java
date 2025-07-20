import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class EscapeMarble2_13460 {
    // dy, dx for up, down, left, right
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] board = new char[N][M];
        int[] R = new int[2];
        int[] B = new int[2];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j);
                if (board[i][j] == 'R') {
                    R[0] = i;
                    R[1] = j;
                    board[i][j] = '.';
                } else if (board[i][j] == 'B') {
                    B[0] = i;
                    B[1] = j;
                    board[i][j] = '.';
                }
            }
        }

        // Queue stores: {r_row, r_col, b_row, b_col, move_count}
        Deque<int[]> q = new ArrayDeque<>();
        boolean[][][][] visited = new boolean[N][M][N][M];

        q.offer(new int[]{R[0], R[1], B[0], B[1], 0});
        visited[R[0]][R[1]][B[0]][B[1]] = true;

        while (!q.isEmpty()) {
            int[] state = q.poll();
            int r_row = state[0];
            int r_col = state[1];
            int b_row = state[2];
            int b_col = state[3];
            int count = state[4];

            if (count >= 10) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nr_r = r_row;
                int nr_c = r_col;
                int nb_r = b_row;
                int nb_c = b_col;

                boolean r_in_hole = false;
                boolean b_in_hole = false;

                // Move blue marble
                while (board[nb_r + dy[i]][nb_c + dx[i]] != '#') {
                    nb_r += dy[i];
                    nb_c += dx[i];
                    if (board[nb_r][nb_c] == 'O') {
                        b_in_hole = true;
                        break;
                    }
                }

                // Move red marble
                while (board[nr_r + dy[i]][nr_c + dx[i]] != '#') {
                    nr_r += dy[i];
                    nr_c += dx[i];
                    if (board[nr_r][nr_c] == 'O') {
                        r_in_hole = true;
                        break;
                    }
                }

                if (b_in_hole) {
                    continue; // If blue marble is in the hole, this is a failure case, so we skip.
                }

                if (r_in_hole) {
                    System.out.println(count + 1);
                    return; // If only red marble is in the hole, we found the solution.
                }

                // If both marbles end up on the same spot, resolve collision.
                if (nr_r == nb_r && nr_c == nb_c) {
                    // The marble that was further from the direction of movement gets pushed back.
                    switch (i) {
                        case 0: // Up
                            if (r_row > b_row) nr_r -= dy[i]; else nb_r -= dy[i];
                            break;
                        case 1: // Down
                            if (r_row < b_row) nr_r -= dy[i]; else nb_r -= dy[i];
                            break;
                        case 2: // Left
                            if (r_col > b_col) nr_c -= dx[i]; else nb_c -= dx[i];
                            break;
                        case 3: // Right
                            if (r_col < b_col) nr_c -= dx[i]; else nb_c -= dx[i];
                            break;
                    }
                }

                if (!visited[nr_r][nr_c][nb_r][nb_c]) {
                    visited[nr_r][nr_c][nb_r][nb_c] = true;
                    q.offer(new int[]{nr_r, nr_c, nb_r, nb_c, count + 1});
                }
            }
        }

        System.out.println(-1); // If queue is empty and no solution was found
    }
}