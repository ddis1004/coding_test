import java.io.*;
import java.util.*;


public class SharkMiddle_21609 {
	static int N;
	static int M;
	static int[][] board;
	static final int BLANK = -3;
	static final int RAINBOW = 0;
	static final int BLACK = -1;
	
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
	private static void rotate() {
		int[][] newBoard = new int[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				newBoard[N - j - 1][i] = board[i][j];
			}
		}
		board = newBoard;
	}
	
	private static void gravityFlush(ArrayList<Integer> list, int x, int y) { // flush f
		for(int i = 0; i < list.size(); i++) {
			board[x - i][y] = list.get(list.size() - i - 1);
		}
		list.clear();
	}
	
	private static void gravity() {
		ArrayList<Integer> temp = new ArrayList<Integer>();
		for(int j = 0; j < N; j++) {
			for(int i = 0; i < N; i++) {
				if(board[i][j] == BLACK){//black
					gravityFlush(temp, i - 1, j); // flush on the black block
				}
				else if(board[i][j] != BLANK) {
					temp.add(board[i][j]);
					board[i][j] = BLANK;
				}
			}
			gravityFlush(temp, N - 1, j);
		}
	}
	
	private static int delLargestBlock() {
		ArrayList<int[]> block = new ArrayList<>();
		ArrayList<int[]> largestBlock = new ArrayList<>();
		ArrayList<int[]> rainbow = new ArrayList<>();
		boolean[][] visited = new boolean[N][N];
		int maxRainbowCount = 0;
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(board[i][j] == RAINBOW) rainbow.add(new int[]{i, j});
			}
		}
		
		ArrayDeque<int[]> queue = new ArrayDeque<int[]>();
		for(int i = 0; i < N; i ++) {
			for(int j = 0; j < N; j ++) {
				if(!visited[i][j] && board[i][j] != RAINBOW && board[i][j] != BLACK && board[i][j] != BLANK) {
					int color = board[i][j];
					queue.offer(new int[] {i, j});
					block.add(new int[] {i, j});
					visited[i][j] = true;
					int rainbowCount = 0;
					while(!queue.isEmpty()) {
						int[] coord = queue.poll();
						for(int d = 0; d < 4; d++) {
							int nx = coord[0] + dx[d], ny = coord[1] + dy[d];
							if(nx >= 0 && nx < N && ny >= 0 && ny < N &&
									!visited[nx][ny] &&(board[nx][ny] == color || board[nx][ny] == RAINBOW)) {
								if(board[nx][ny] == RAINBOW) rainbowCount ++;
								visited[nx][ny] = true;
								block.add(new int[] {nx, ny});
								queue.offer(new int[] {nx, ny});
							}
						}
					}

					if(block.size() >= 2){
						if( block.size() > largestBlock.size() ) {
							largestBlock = block;
							maxRainbowCount = rainbowCount;
						} else if ( block.size() == largestBlock.size() && rainbowCount >= maxRainbowCount){
							largestBlock = block;
							maxRainbowCount = rainbowCount;
						}
					}
					block = new ArrayList<>();
					for(int k = 0; k < rainbow.size(); k++) { //reset rainbow visited
						int[] coordr = rainbow.get(k);
						visited[coordr[0]][coordr[1]] = false;
					}
				}	
			}
		}
		for(int i = 0; i < largestBlock.size(); i++) {
			int[] coord = largestBlock.get(i);
			board[coord[0]][coord[1]] = BLANK;
		}
		return largestBlock.size() * largestBlock.size();
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][N];
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < N; j ++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int score = 0;
		
		while(true) {
			int tScore = delLargestBlock();
			score += tScore;
			if(tScore == 0) {
				System.out.println(score);
				return;
			}
			gravity();
			rotate();
			gravity();
		}
		
		
	}
}
