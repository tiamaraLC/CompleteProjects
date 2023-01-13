import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class WikiRacer {

	/*
	 * Do not edit this main function
	 */
	public static void main(String[] args) {
		List<String> ladder = findWikiLadder(args[0], args[1]);
		System.out.println(ladder);
	}
			
		
		
	/*
	 * Do not edit the method signature/header of this function
	 * TODO: Fill this function in.
	 */
	private static List<String> findWikiLadder(String start, String end) {
		int count = 0;
//		System.out.println("start page is: " +start);
//		System.out.println("end page is: "+ end);
		MaxPQ q = new MaxPQ();
//		Set<String> temp = WikiScraper.findWikiLinks(start);
		Set<String> target = WikiScraper.findWikiLinks(end);
//		System.out.println(temp);
		//System.out.println(target);
		List<String> ladder = new ArrayList<>();
		//["Fruit"]
		ladder.add(start);
		int priority = getPriority(start, target);
		q.enqueue(ladder, priority);
//		System.out.println(q.size());
//		System.out.println("the queue is...." +q.toString());
		while(!q.isEmpty()) {
			// returns the highest priority of the partial ladder
			List<String> curr = q.dequeue();
//			System.out.println("curr is ladder: "+ curr);
			// current page in partial ladder
			String currPage = q.currPage(curr);
//			System.out.println("curr page in sub: " + currPage);
			// set of links on the current page
			Set<String> sub = WikiScraper.findWikiLinks(currPage);
//			System.out.println("sub ladder of curr: " + sub);
			if (sub.contains(end)) {
				curr.add(end);
//				System.out.println("final ladder1: " +curr);
				return curr;
			}
			// for each pach in the currPage link set
			for (String page: sub) {
				// If this neighbor page hasn’t already been visited:
				if (!ladder.contains(page)) {
					// copy the curr partial ladder
					List<String> copy = new ArrayList<>();
//					System.out.println("copy ladder: " +copy);
					// Put page in the copied ladder
					copy.add(start);
					copy.add(page);
					
					int p = getPriority(page, target);
					q.enqueue(copy, p);
//					System.out.println("the queue is...." +q.toString());
					
					
					
				}
				
			}
		}
		
//		System.out.println("FINAL ladder2: " +ladder);
		return ladder;
	}

	
	private static int getPriority(String curr, Set<String> target ) {
//		System.out.println("curr to count: " +curr);
//		System.out.println("the target is: " +target);
		int count = 0;
		if (target.contains(curr)) {
			count ++;
		}
//		System.out.println(curr+"...."+count);
		return count;
		
	}

}
