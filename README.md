# Quote topic guesser

## What is it? 
This project is a small **Python** project I used to train several skills:
- scraping websites with `scrapy`
- Working on json datasets with `Pandas`
- Using ML with `sickit-learn`

## What is it composed of
The folder tutorial contains all the scrapy elements. 
It was created by following the scrapy tutorial, but I then used 
the website **goodread** to have a bigger dataset. The spider 
exports the extracted quotes, with author and tags to the file
`quotes.json`.

The quote_analysis.ipynb is used to:
- extract the data from the json into a dataframe
- transform the quotes text to TF-IDF vectors
- binarize the tags (as there can be multiple of them)
- create a model 
- dump the model, vector and multi-label binarizer

Finally, the predict_tags file loads the three dumped objects.
It then waits for user input to try to predict the tags of a new 
quote.

