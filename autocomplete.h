#ifndef __AUTOCOMPLETE_H__INCLUDED__
#define __AUTOCOMPLETE_H__INCLUDED__


#include <stdio.h>


typedef struct WordList WordList;
struct WordList
{
    int    count;
    int    alloc;
    char **words;
};



typedef struct LookupTreeNode LookupTreeNode;
struct LookupTreeNode
{
    /* 
     *
     * This field must be an array of 26 pointers.  An actual
     * array of pointers, declared here (not a pointer-pointer)
     */
    LookupTreeNode *children[26];
    /* see the WordList type (with its associated functions) above. */
    WordList *result_words;
};



WordList *wl_create (void);
int       wl_add    (WordList *list, char *word);
void      wl_destroy(WordList *list);

LookupTreeNode *ltn_create(void);
void            ltn_add_result_word(LookupTreeNode *ltn, char *search_word, char *result_word);
void            ltn_destroy(LookupTreeNode *ltn);

int node_count  (LookupTreeNode *root);
int result_count(LookupTreeNode *root);

LookupTreeNode *lookup(LookupTreeNode *root, char *search);

WordList       *build_wordlist_from_file(FILE *fp);
LookupTreeNode *build_tree_from_words   (WordList *words);
void            print_words(LookupTreeNode *result, char *search);



#endif     // __AUTOCOMPLETE_H__INCLUDED__


