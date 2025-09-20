import java.io.*;
import java.util.*;

public class Surveilence_15683 {

    static ArrayList<int[]> cameras = new ArrayList<>();
    static int answer = Integer.MAX_VALUE;
    static int N, M;

    // Direction arrays: Up, Right, Down, Left
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };

    private static int countBlank(int[][] room) {
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (room[i][j] == 0) {
                    count++;
                }
            }
        }
        return count;
    }

    private static void fill(int x, int y, int dir, int[][] room) {
        dir %= 4;
        while (true) {
            x += dx[dir];
            y += dy[dir];

            if (x < 0 || x >= N || y < 0 || y >= M || room[x][y] == 6) {
                break;
            }

            if (room[x][y] == 0) {
                room[x][y] = 9;
            }
        }
    }

    private static void dfs(int camIndex, int[][] currentRoom) {
        // Base case: All cameras have been placed.
        if (camIndex == cameras.size()) {
            answer = Math.min(countBlank(currentRoom), answer);
            return;
        }

        int[] currentCam = cameras.get(camIndex);
        int type = currentCam[0];
        int x = currentCam[1];
        int y = currentCam[2];

        // Try all possible rotations for the current camera.
        for (int i = 0; i < 4; i++) {
            // Create a deep copy of the current room state.
            int[][] nextRoom = new int[N][M];
            for (int r = 0; r < N; r++) {
                System.arraycopy(currentRoom[r], 0, nextRoom[r], 0, M);
            }

            // Apply surveillance based on camera type.
            switch (type) {
                case 1:
                    fill(x, y, i, nextRoom);
                    break;
                case 2:
                    fill(x, y, i, nextRoom);
                    fill(x, y, i + 2, nextRoom);
                    break;
                case 3:
                    fill(x, y, i, nextRoom);
                    fill(x, y, i + 1, nextRoom);
                    break;
                case 4:
                    fill(x, y, i, nextRoom);
                    fill(x, y, i + 1, nextRoom);
                    fill(x, y, i + 2, nextRoom);
                    break;
                case 5:
                    fill(x, y, 0, nextRoom);
                    fill(x, y, 1, nextRoom);
                    fill(x, y, 2, nextRoom);
                    fill(x, y, 3, nextRoom);
                    break;
            }

            // Recurse to the next camera with the new room state.
            dfs(camIndex + 1, nextRoom);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[][] room = new int[N][M];

        for (int i = 0; i < N; i++) {
            StringTokenizer tokenizer = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int space = Integer.parseInt(tokenizer.nextToken());
                if (space > 0 && space < 6) {
                    cameras.add(new int[]{space, i, j});
                }
                room[i][j] = space;
            }
        }

        dfs(0, room);
        System.out.println(answer);
    }
}