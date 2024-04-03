transcript = """Speaker 4
Yeah, I think for now I don't want to do any more sort of, hey, this would be admin. 

Speaker 2
Before we. 

Speaker 4
Get a client because right now that would be a 5% better thing where we need to focus on the things that can get us 50% better. 

Speaker 2
That's a very good point. Yeah. 

Speaker 3
Have you figured out the LinkedIn scripture issue? 

Speaker 2
I did, actually. Kind of. There's progress. Let me show you. We have three options. This is the one that I was looking at yesterday. Maybe they emailed me back. 

Speaker 2
There'S bright data them, there's relevance AI apparently, and phantom busters. And I love relevance. So we good start there for an initial build and it's very easy to integrate into GPT, which is the really cool part. How much have you played with relevance? 

Speaker 3
I played with. 

Speaker 2
Sorry, suddenly I can't quite hear you. Okay, there we go. 

Speaker 2
Let's see. We're talking tools, templates. LinkedIn scraper is how compatible job candidate improve LinkedIn post company research. Scrape Lincoln's profile. Get someone's professional data from LinkedIn profile. 

Speaker 2
So we get an about section. We get followers count, full name headline hqcDHQ country where are you? Okay, so this does not contain posts education experiences. More companies, more companies. Okay, and now we're getting user posts. But you see how this is an agent by itself, which has actions that it can do. It just doesn't get to choose which actions it does. 

Speaker 2
We're absolutely over the moon. We have broken ground and snowman apartment is going ahead. So they're building new apartments for this ski place. 
"""


#Cut the conversation every 5 speakers and apply an overlap of 1

split_transcript = transcript.split("Speaker")
print(split_transcript)

final_chunks = []
for i, speaker in enumerate(split_transcript):
    #i modulus 3 is 0
    if i % 5 == 0:
        print(split_transcript[i])
        final_chunks.append(split_transcript[i-5:i])

import pprint
pprint.pprint(final_chunks)
    

