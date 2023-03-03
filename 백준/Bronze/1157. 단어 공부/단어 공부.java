import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	static class Element implements Comparable<Element>{
		public int count;
		public char alphabet;
		
		public Element(char alphabet) {
			this.count = 0;
			this.alphabet = alphabet;
		}

		@Override
		public int compareTo(Main.Element o) {
			return o.count - this.count;
		}
	}
	
	public static void main(String[] args) throws IOException {
		String words = br.readLine();
		words = words.toUpperCase();
		List<Element> elements = new ArrayList<>();
		for (char c = 'A'; c <= 'Z'; c++) {
			elements.add(new Element(c));
		}
		
		for (int i = 0; i < words.length(); i++) {
			elements.get(words.charAt(i) - 'A').count++;
		}

		Collections.sort(elements);
		if (elements.get(0).count == elements.get(1).count) {
			System.out.println("?");
		} else {
			System.out.println(elements.get(0).alphabet);
		}
		
	}
}
