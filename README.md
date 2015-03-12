# neighborhood
redefine neighborhoods by home features

-----------------
project description
-----------------
A 4-part problem using my company's real estate listings data/history for San Francisco and East Bay, described below. I intend to complete parts 1 and 2, with 3 and 4 being extra credit in case I blow through it quickly.

#### 1. Clustering (after preprocessing with feature extraction or selection)
Define 'neighborhoods' in terms of similar-price, similar-home-feature clusters. Not sure yet whether geographical proximity should be a factor, probably will try with and without. If clustering turns out to be irascible or un-illuminating, I can convert to classification by training the data with the lat/long that users are conducting their home searches in. Either reduce dimensions or use user data to select features (e.g. users are set on their bedroom count).

#### 2. Text-mine descriptors to label the clusters
Text-mine listing descriptions and/or geo-tagged social media posts to describe clusters -- I'm fascinated by how apps like Yelp, Glassdoor, Amazon, LinkedIn etc are able to pull out the 'key point/insight' in customer reviews, and would like to replicate that. e.g. "Oh what we think of as Nob Hill should have its western boundaries extended if we think in terms of home price affordability." Either do n-grams (with listing descriptions) or identify which sentences have the highest cumulative tf-idf from words (most unique sentence), or find which words are tied to topic sentences.

#### 3. Use APIs
Use restaurant & bar data as another dimension in determining the clusters and/or as the labels instead in a classification exercise -- I basically want opening hours and type of establishment (luxury, dive etc). I could pull this from Yelp, Google Maps or OpenTable's API if available, or just our company-purchased restaurant map layers if that becomes too gnarly.

Also, use Google Elevation API to enrich the data with altitude and identify hills

#### 4. Predict future gentrification, pockets of home price growth
Understand how the clusters evolve, especially with regard to gentrification. If whatever I did for 1. didn't produce recommendations or a similarity distance metric (i.e. if I used geographic proximity), then also do this (i.e. 'if you like homes in Nob Hill cluster, you'll also like this random neighborhood in San Jose').

------------
data
------------
~~all single-family residences, condos and townhouses sold in the 9-county SF Bay Area between May 1, 2014 and Aug 31, 2014~~
all homes in the 9-county SF Bay Area that were assessed for property taxes at some point in 2009
