/*
 * Author: Tiamara Craig
 * File autocomplete.c
 * Description: This program works to implement the WordList Struct 
 * described in the autocomplete.h file. This program models
 * a growing array of string pointers.
 */






#include <stdlib.h>
#include <stdio.h>
#include "autocomplete.h"
#include <string.h>




/*
 * Purpose: Creates two malloc()ed buffers: 
 * one for the struct itself, and one for the array of pointers
 * Param: NULL
 * Return: An array of string pointers, type WordList
 */
WordList * wl_create (void) {
	// array for the struct WordList
	WordList * list = malloc(sizeof(WordList));
	// the array of pointers
	list->words = malloc(4*sizeof(char*));
	// malloc() error checking
	if(list->words == NULL|| list == NULL) {
		printf("Could not malloc arrary(s)");
		return NULL;
	}
	list->count = 0;
	list->alloc = 4;
	return list;
}




/*
 * Purpose: free()'s both buffers that were created w/o freeing the 
 * strings themselves
 * Param: *list, type WordList
 * Return: NULL
 */
void wl_destroy(WordList *list) {
	// free the array of pointers, words
	free(list->words);
	// reset the alloc & word counter
        list->count = 0;
	list->alloc = 4;
	// free the array for the stuct
	free(list);
}




/*
 * Purpose: realloc()ates the array buffer by doubling its size
 * Param: *list, type WordList
 * Return: 0 | 1 - error code where 1 = failure  & 0 = works properly
 */
int growArray(WordList *list) {
	int error_code = 0;
	list->alloc = list->alloc * 2;
	list->words = realloc(list->words, list->alloc * sizeof(char*));
	if(list->words == NULL) {
		error_code = 1;
	}
	return error_code;

}




/*
 * Purpose: Adds a new word to the list, and realloc()ates the buffer if
 * needed
 * Param: *list, type WordList & a *word type char 
 * Return: 0 | 1 - error code where 1 = failure  & 0 = works properly
 */
int wl_add(WordList *list, char *word) {
	int error_code = 0;
	// if the buffer is not large enough, growArray()
	if(list->count == list->alloc) {
		error_code = growArray(list);
	}
	// add the word ptr to the end of the words list
	
	list->words[list->count] = word;
	// update count
	list->count = list->count + 1;
	return error_code;
}


/*
 * Purpose: Adds a new word to the list from a file, and realloc()ates the buffer if
 * needed
 * Param: *fp, type FILE
 * Return: An array of string pointers, type WordList
 */
WordList *build_wordlist_from_file(FILE *fp) {
        // error checking for file
        if(fp == NULL) {
                fprintf(stderr, "Opening file failed with code.\n");
                return NULL;

        }
        // create WordList
        WordList * list = wl_create();
        char * word = NULL;
        char line[256];
        // loop over lines in file
        while(fgets(line, 256, fp) != NULL) {
                if(strcmp(line, "\n")) {
                        for(int i=0;line[i]!='\n';i++){
                                // covert to uppercase
                                if(line[i] > 96 && line[i] < 123) {
                                        line[i] -= 32;
                                }
                                // create a buffer for each word/ string
                                word = (char*)malloc(strlen(line+1)*sizeof(char));
                                strcpy(word, line);
                        }
                        // add *word to WordList
                        wl_add(list, word);
                }
        }
        fclose(fp);
        return list;
}



