# Readme

## Milestones

#### Dataset 
- Split the dataset into a training set for the AI model and a set that will be used as the seed lyrics for Turkers to come up with the next line. This same set will be used when we ask Turkers if the Turker responses or the AI generated lyrics produce a better lyric.  
- Score: 3
  - We’re going to need to manually go through the dataset and create a training set that is representative of the database as well as a representative dataset for testing the model and turkers. 

#### Create and test AI model
- Training and developing a model that outputs the next song lyric line that would follow the seed lyric. We will train the model on the subset of the kaggle created in the above milestone for testing.  
- Score: 2
  - We have a starter code but need to train the model and alter it

#### Give starter lyrics to turkers
- Create a set of HITs to give to Turkers as outlined above. For each lyric we are going to ask Turkers to continue the song and write five lyrics to continue the song. For each lyric we are going to have 3 Turkers continue the song. 
- Score: 2
  - We have to aggregate the song lyrics into a csv

#### Give starter lyrics to AI model
- Give the starter lyrics to the AI model and record the output the trained model results
- Score: 1

#### Quality control 
- Create another HIT to filter out “undesirable” turker responses. For each lyric given by a Turker, ask another Turker whether the lyrics are written in coherent english. Use a majority rating system to determine whether a lyric is accepted, if a lyric is rejected remove it from the dataset. 
- Score: 3
  - Must create HIT and then use data from HIT  to score each response and remove “bad” reponses


#### Aggregation module
- Combine the AI responses and turker responses into one dataset. Create another HIT and have turkers vote on which response is better given the starter lyrics - they are presented with an AI response and turker response but do not know which one is which.
- Score: 3
  - Must aggregate data in way that combines all responses while still preserving which response is from the AI and which is from a Turker

#### Analyze findings  
- We will analyze the results from the final HIT. This will enable us to compare the success rates of AI-generated lyrics against people-generated lyrics. We hope this analysis will help determine what role AI could play in songwriting and how it could be incorporated into tools to help professional songwriters, aspiring artists, or a serenading lover ;).
- Score 2:
  - Much of this analysis will be calculating the number of times an AI-lyric was chosen over a person-generated lyric. However, this may also include analyzing the success rate of specific AI-generated lyrics against other AI-generated lyrics and/or researching relevant songwriting tools that can incorporate AI.  
