

CODE FLOW OF SENTIMENT ANALYSIS
===============================

library used
^^^^^^^^^^^^

	Textblob: library used for nlp purpose.
	tweepy: tweeter API for fetching tweets.


installing dependencies
^^^^^^^^^^^^^^^^^^^^^^^

dependencies can be installed using pip or pip3::

	>> pip install Textblob tweepy
	>> pip3 install Textblob tweepy

code steps
^^^^^^^^^^

	* Register and get consumer token, consumer secret, access token, access token secret.
	* Authenticate your API using above keys from tweepy.auth() function.
	* Input for keywords of interest.
	* API search for public posts related to topic.
	* Applying textblob to tweets and measuring their sentiment polarity.

