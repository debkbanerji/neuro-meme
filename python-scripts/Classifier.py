import time

import database_interface

from MemeScraper import RedditScraper
import database_interface
from NeuralNet import buildNeuralNet

subreddits = ['ProgrammerHumor', 'wholesomememes', 'memes']
subreddits = ['memes']

# millis = int(round(time.time() * 1000))

scaling_factor = 1000  # Dividing  because numbers are too big


def pack_meme(meme):
    xVals = [
        # (millis - meme['created_utc']) / 6.048e+8,
        int(meme['downs'] / scaling_factor),
        int(meme['num_comments'] / scaling_factor),
        int(meme['score'] / scaling_factor),
        int(meme['ups'] / scaling_factor),
    ]
    yVals = [
        meme['dankness'],
        meme['spiciness']
    ]
    return (xVals, yVals)


# print(database_interface.get_train())

examples = []

rawExamples = database_interface.get_train()
for trainExample in rawExamples:
    example = rawExamples[trainExample]
    meme = pack_meme(example)
    print(meme)
    examples.append(meme)
    # print(pack_meme(trainExample))

numExamples = examples.__len__()
# print(numExamples)

# print(examples)
trainExamples, testExamples = examples[:int(examples.__len__() / 2)], examples[int(examples.__len__() / 2):]

nnet, accuracy = buildNeuralNet((trainExamples, testExamples), alpha=0.1, weightChangeThreshold=0.00000008,
                                hiddenLayerList=[], maxItr=20000,
                                startNNet=None)

print(accuracy)

scraper = RedditScraper()

for subreddit in subreddits:
    result = scraper.scrape_subreddit(subreddit, 200)
    for item in result:
        packed_meme = pack_meme(item)
        feedForwardResult = nnet.feedForward(packed_meme[0])
        # print(pack_meme(item))
        item['dankness'] = int(round(1000 * feedForwardResult[-1][0], 0))
        item['spiciness'] = int(round(1000 * feedForwardResult[-1][0], 1))
        # item['dankness'] = feedForwardResult[-1][0]
        # item['spiciness'] = feedForwardResult[-1][0]
        print(item)
        database_interface.upload_classified_meme(item)

# print(database_interface.get_train())
