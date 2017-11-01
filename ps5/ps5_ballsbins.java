import java.io.*;
import java.util.concurrent.ThreadLocalRandom;

public class ps5_ballsbins {
	private static int bins() {
		int[] B = new int[50];
		B[0] = 1000000000;

		for (int i = 0; i < 1000000000; i++) {
			int rand = ThreadLocalRandom.current().nextInt(0, 1000000000);
			if (rand <= B[0]) {
				B[1] += 1;
				B[0] -= 1;
			}
			else {
				int counter = 0;
				while (((rand - B[counter - 1]) > B[counter]) && (counter < 50)) {
					counter += 1;
				}

				if (rand <= B[counter]) {
					B[counter + 1] += 1;
					B[counter] -= 1;
				}
			}
		}

		int max_load;
		for (int i = 0; i < 50; i++) {
			if B[i] > 0 {
				max = i;
			}
		}
	return max;
	}
}

public class ps5_ballsbins_modified {
	private static int bins() {
		int[] B = new int[50];
		B[0] = 1000000000;

		for (int i = 0; i < 1000000000; i++) {
			int rand1 = ThreadLocalRandom.current().nextInt(0, 1000000000);
			int rand2 = ThreadLocalRandom.current().nextInt(0, 1000000000);
			if (rand1 < rand2) {
				rand = rand1;
			}
			else {
				rand = rand2;
			}
			
			if (rand <= B[0]) {
				B[1] += 1;
				B[0] -= 1;
			}
			else {
				int counter = 0;
				while (((rand - B[counter - 1]) > B[counter]) && (counter < 50)) {
					counter += 1;
				}

				if (rand <= B[counter]) {
					B[counter + 1] += 1;
					B[counter] -= 1;
				}
			}
		}

		int max_load;
		for (int i = 0; i < 50; i++) {
			if B[i] > 0 {
				max = i;
			}
		}
	return max;
	}
}