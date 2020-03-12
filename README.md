# Googling for Representatives

An investigation of how likely it is that googling for the name of your congressional representative returns the name of an incorrect representative. 

I've highlighted some more incorrect results in "More Incorrect SERP examples.pdf", but see the potential_mistakes CSV files for more. 

## In this Repo:

### Collected results (in `results`) 
Results labled 1_14 were collected January 14-15, 2020. Results labeled 3_9 were collected March 9 - 10. More data will be added soon. 

See the About the Data section for details about the data methods of collection.

-  [Drive link to static copies of the SERP html pages](https://drive.google.com/drive/folders/16sepdh8zUGjF9fcJv67ej9ds8WifZyFw?usp=sharing)
- `3_9_zipcode_potential_mistakes.csv`, `1_14_potential_mistakes.csv`: files containing then names of other congressional representatives that appear in the top result.

### Code
SERP collection code and analysis code (to be further cleaned up on a future date)


## About the Data: 
Previous research has established both query formulation  to be influential in determining search engine results. Therefore, the data collection approach is designed to assess whether inaccuracies in representative names are persistent for individual representatives across various search terms and query formulations. However our list is not exhaustive.


### Query terms: 
See the final 40 columns of `data/cong_queries` for the variations of queries used to search for representatives' names by congressional district. 

For zip codes, I used 4 variations  for 1917 randomly sampled zipcodes (with the constraint that at least 2 zip codes must come from within 1 congressional district):
- zip code + representative; zip code + rep; zipcode + congress; zipcode + congressperson

The full set of zip code queries are in `data/zip_queries`

### What counts as "incorrect"
I define an incorrect result as one that lists a name that does not belong to the elected representative of that district in the top position of the SERP.

- If multiple names are listed that include the representative's name, I do not count this as incorrect
- If an incorect name is listed, but they are not a current congressional representative, I do not count this as incorrect (there are some false positives where this occurs... and this should probably be counted as incorrect)  

While there are certainly some false positives, some informal manual validation indicates that this criteria has actually undercounted misleading/incorrect SERPs. Hoping to follow up with some formalizations of this. 



