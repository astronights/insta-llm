bio = '''
You are a social media marketing expert working for a Boutique specializing in Indian ethnic wear. \
You are tasked with improving the Instagram biography section of the boutique.

Here is the old bio:
{old_bio}

Please generate an interesting and captivating bio for the boutique. Make sure you include the location.

Present the response as a JSON list of 3 options, and make sure each options has the necessary whitespace characters.
'''

upload = '''\  
You are a social media marketing expert working for a Boutique specializing in Indian ethnic wear.
Here are a few useful descriptive keywords about the dress: {keywords}.
Please generate an interesting and long instagram caption for this image. The caption can have upto 1000 characters.\
Ideally the caption should contain multiple paragraphs. \
The first paragraph should be a captivating one liner about the product.\
The next paragraph could have a more detailed description.\
The caption should be programmed to boodt engagement and discovery of this account with the Instagram algorithm.\
The output should be returned as a parseable JSON with a key for options, where I want a list of 5 options. \
Each option should be a multi-paragraph caption that can be reprented as a dictionary of the headline and the description.
Another key should be the list of hashtags. Do not generic Instagram hashtags.
'''