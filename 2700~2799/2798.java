//블랙잭
//파일명 Main으로 변경 후 실행
//package bjoj.p2798.blackjack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.Arrays;

class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String num[] = br.readLine().split(" ");
		
		int N = Integer.parseInt(num[0]);//ī�� ��
		int M = Integer.parseInt(num[1]);
		int[] arr = new int[N];
		int answer = Integer.MIN_VALUE;
		
		String num2[] = br.readLine().split(" ");
		
		for(int i=0; i<N; i++) {
			arr[i] = Integer.parseInt(num2[i]);			
		}
		
		for(int i=0; i<arr.length-2; i++) {
			for(int j=i+1; j<arr.length-1; j++) {
				for(int k=j+1; k<arr.length; k++) {
					int sum = arr[i]+arr[j]+arr[k];					
					if(sum<=M) {
						answer = sum>answer?sum:answer;
					}
				}
			}
		}		
		System.out.println(answer);
	}
}
