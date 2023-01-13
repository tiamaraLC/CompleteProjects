import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Set;





/*
 * TODO: This file should contain your priority queue backed by a binary
 * max-heap.
 */
public class MaxPQ {
	
	private Ladder array[];
    private int size;
    private int capacity;
    private int pos;

	    /*
	     * In this constructor should initialize a new
	     * empty queue that does not contain any patients.
	     * Initially the queue’s internal heap array should
	     * have a capacity of 10 elements. The front-most element
	     * is stored at index 1 in your array.
	     */
    public MaxPQ() {
        array = new Ladder[10];
        capacity = 10;
        size = 0;
        pos = 1;
        
    }
    
    
	// memorizaton in scaper
	// ^^ save the links in a hashmap
	public void enqueue(List<String> page, int priority) {
		Ladder ladder = new Ladder(page, priority);
		if (size >= capacity) {
            // the fxn to expand array capacity
            this.growArray();
        } else {
            // loop over the array
            for (int i = 0; i <= size; i++) {
                if (isEmpty()) {
                    array[pos] = ladder;
//                   System.out.println("ladder: " +ladder);
                    size++;
                    pos++;
                    break;
                } else {
                    // place new patient at the end of queue
                    if (array[pos] == null) {
                        array[pos] = ladder;
                        System.out.println(ladder);
//                        System.out.println(toString());
                        // init the parent ands its children
                        int child = pos;
                        int parent = child / 2;
                        
                        // determine if you need to bubble up
                        while (array[child].priority < array[parent].priority
                                && parent != 0) {
                            bubbleUp(parent, child);
                        }
                        pos++;
                        size++;
                        break;
                    }

                }
            }
        }
    }
	
	
	public void setSize() {
		size +=1;
	}
	
	
	


	 /*
     * In this function you should remove the front-most
     * patient in your queue, and return their page as a string.
     * You should throw an exception if the queue is empty.
     */
    public List<String> dequeue() {
        Ladder first = array[1];
        if (isEmpty()) {
            return null;
        } else {
        	//Ladder max_p = array[1];
            // make the last item in the queue the first;
            array[1] = array[size];
            // remove last item
            array[size] = null;
            size -=1;
            if (size > 0) {
            	int pos = 1;
            	Ladder curr = array[1];
            	while (pos * 2 <= size) {
            		int child = pos*2;
            		if (child != size && array[child+1].priority > array[child].priority) {
            			child += 1;
            		}
            		if (array[child].priority > curr.priority) {
            			array[pos] = array[child];
            			pos = child;
            		} else {
            			break;
            		}
            		array[pos] = curr;
            		
            	}
            }
//            System.out.println(first);
            
            return first.getLadder();
           
        } 
        //return first.page;
    }
		
	/*
     * the function moves a child up the priority queue
     * in order restore the order of the min priority heao;
     */
    private void bubbleUp(int child, int parent) {
        Ladder l_temp = array[parent];
        array[parent] = array[child];
        array[child] = l_temp;



    }
    
    private void bubbleDown(int child, int parent) {
        // swap the parent and its child
        Ladder l_temp = array[parent];
        array[parent] = array[child];
        array[child] = l_temp;

    }
    
    

    /*
     * This function expands the array one the size has reached
     * max capacity
     */
    private void growArray() {
        Ladder[] newArray = new Ladder[capacity * 2];
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
        capacity *= 2;
    }
    
//    public Set<String> getCurrLink() {
//    	Set<String> curr = new HashSet<String>();
//    	Ladder currLadder  = peekPriority();
//    	
//    	
//    	
//    }
//    
//    	
//	public Ladder peekPriority() {
//		if (isEmpty()) {
//            throw new NoSuchElementException();
//        }
//        return array[1];
//
//    }
    	
    
	public boolean isEmpty() {
		return size == 0;
	}
	
	public int size() {
		return size;
	}
	
	public String currPage(List<String> curr) {
		return (curr.get(curr.size()-1));
		
	}
	
	public String toString() {
        String result = "{";
        for (int i = 0; i < array.length; i++) {
            if (array[i] != null) {
                result += array[i] + ", ";
            }
        }
        result += "}";
        return result;

    }

	
	
	/*
     * Private class that stores information about a Pages ladder
     *  in the Max_PQ
     */
	private class Ladder {

	    public List<String> page;
	    public int priority;

	    public Ladder(List<String> page, int priority) {
	        this.page = page;
	        this.priority = priority;
	    }
	    
	    public List<String> getLadder() {
	    	return this.page;  	
	    }
	    
//	    public String getCurr () {
//	    	return page.get(page.size());
//	    }

	    public String toString() {
	    	return page +  "->" + priority;
	    }


	}


}


