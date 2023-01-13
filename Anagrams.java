/*
 * 
 * Author: Tiamara Craig
 * 
 * This program works to find the anagrams of given word using
 * a dictionary file of possible anagrams. Using recursive 
 * backtracking, the program is able to find all find all the 
 * possible anagrams -- words that can be formed from the original
 * word-- by keeping a detailed reported of the number of 
 * characters in the original string as well it size, etc.
 * stored in the given class: LetteryInventory
 * 
 * 
 * The command line arguments should include a dictionary file,
 * a target word and a max amount of anagrams, 0 included
 * 
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class PA12Main {

    /*
     * main: calls the methods below in the order
     * prescribed
     * 
     * @param: comoand line arguments
     */
    public static void main(String[] args) {
        // empty list to store anagrams
        List<String> anagram = new ArrayList<>();
        List<String> dict = read(args[0]);
        LetterInventory li = new LetterInventory(args[1]);
        // possible: the min dict of words needed to be found in the
        // Original word
        List<String> possible = collectPoss(dict, li, args[1]);
        process(possible, li, anagram, Integer.valueOf(args[2]));
    }

    /*
     * read: reads the dictionary file from the command
     * line
     * 
     * @param: the string fname (file name)
     * 
     * @return: a list of all words in the dict file
     */
    public static List<String> read(String fname) {
        List<String> dict = new ArrayList<>();
        Scanner file = null;
        // try/catch block to catch any invalid file inputs
        try {
            file = new Scanner(new File(fname));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        while (file.hasNext()) {
            dict.add(file.next());
        }

        return dict;
    }

    /*
     * collectPoss: stores a smaller collection of the possible
     * anagrams that could be found in the original word
     * 
     * @param: dict
     * 
     * @param: li (letterInventory obj)
     * 
     * @param:word
     * 
     * @return: a minimum dict of words that could form an anagram
     */
    public static List<String> collectPoss(List<String> dict,
            LetterInventory li, String word) {
        System.out.println("Phrase to scramble: " + word + "\n");
        // a list of possible anagrams
        List<String> possible = new ArrayList<String>();
        /*
         * loop over the words in dict and save them in
         * list possible
         */
        for (String w : dict) {
            if (li.contains(w)) {
                String choose = w;
                possible.add(choose);
            }
        }
        System.out.println("All words found in " + word + ':');
        System.out.print(possible + "\n");
        System.out.println();
        System.out.println("Anagrams for " + word + ":");
        return possible;
    }

    /*
     * process: uses recursive backtracking to find the possible
     * anagrams
     * 
     * @param: mindict
     * 
     * @param: li (LetterInventory obj)
     * 
     * @param: anagram
     * 
     * @param: max
     * 
     */
    public static void process(List<String> mindict, LetterInventory li,
            List<String> anagram, int max) {
        // base case
        if (li.isEmpty()) {
            // prints the correct list that match the
            // max anagrams indicated
            if (anagram.size() == max) {
                System.out.println(anagram);
            } else if (max == 0) {
                System.out.println(anagram);
            }
        }
        // loop over each word in mindict
        for (String w : mindict) {
            // choose
            String choose = w;
            // check if it is a possible anagram
            if (li.contains(choose)) {
                anagram.add(choose);
                li.subtract(choose);
                // explore
                process(mindict, li, anagram, max);
                // unchose
                li.add(choose);
                anagram.remove(choose);
            }

        }

    }


}
