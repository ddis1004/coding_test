import java.io.*;
import java.util.*;

public class SharkElementry_21608 {
	static int[][] board;
	static int[][] preference;
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {-1, 1, 0, 0};
	static int N;
	
	private static int countPref(int x, int y, int studentIdx) {
		int count = 0;
		for(int d = 0; d < 4; d++) {
			int nx = dx[d] + x;
			int ny = dy[d] + y;
			if(nx >= 0 && nx < N && ny >= 0 && ny < N) {
				for(int i = 0; i < 4; i++) {
					if(preference[studentIdx][i] == board[nx][ny]) {
						count ++; break;
					}
				}
			}
		}
		return count;
	}
	
	private static int countBlank(int x, int y) {
		int count = 0;
		for(int d = 0; d < 4; d++) {
			int nx = dx[d] + x;
			int ny = dy[d] + y;
			if(nx >= 0 && nx < N && ny >= 0 && ny < N) {
				if(board[nx][ny] == 0)
					count ++;
			}
		}
		return count;
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new int[N][N];
		preference = new int[N*N + 1][4];
		int[] placeOrder = new int[N*N];
		
		for(int i = 0; i < N*N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			placeOrder[i] =  Integer.parseInt(st.nextToken());
			for(int j = 0; j < 4; j++) {
				preference[placeOrder[i]][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		/*
		비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
		1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
		2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
		*/
		for(int i = 0; i < N*N ; i++) {
			int placeX = -1, placeY = -1;
			int blankCount = -1, prefCount = -1;
			int target = placeOrder[i];
			//step1. preference check.
			for(int x = 0; x < N; x++) {
				for(int y = 0; y < N; y++) {
					if(board[x][y] != 0) continue;
					int b = countBlank(x, y);
					int p = countPref(x, y, target);
		
					if(p > prefCount) {
						placeX = x; 
						placeY = y;
						prefCount = p;
						blankCount = b;
					} else if (p == prefCount) {
						if(b > blankCount) {
							placeX = x; 
							placeY = y;
							prefCount = p;
							blankCount = b;
						} 
					}
				}
			}
			board[placeX][placeY] = target;		
		}
		
		int answer = 0;
		for(int x = 0; x < N; x++) {
			for(int y = 0; y < N; y++) {
				int count = countPref(x, y, board[x][y]);
				if(count != 0) {
					answer += Math.pow(10, count - 1);
				}
			}
		}
		System.out.println(answer);
	}
}
