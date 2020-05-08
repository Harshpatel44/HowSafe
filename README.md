# News
<h2>Data cleaning</h2>
1. Remove all unwanted characters
2. Remove duplicates in the tokens
3. Lematize the words before finding frequency of them
4. Remove numbers and symbols from frequency of words
5. Remove the pos tags (removed tags [VBD, IN, DT] and removed unwanted words from tags [JJ,NN,NNS], kept [JJS] unchanged. )
6. Remove stop words
7. Find frequency of words
8. count 2-gram and 3-gram frequency of words
9. Remove all the 2 letter words

Notes:
First I planned to remove the some POS_TAG words from the list, but
I need to remove all the unwanted words of all the tenses using lematizing
bi-gram and tri-grams need to be created.