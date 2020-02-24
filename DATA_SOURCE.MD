Queried from Youtube's API on Sunday Feb 23, 9:35PM (Each page consists of 50 results for a total of 200 results)

# cURL Request Made for Page 1
curl\
'https://www.googleapis.com/youtube/v3/videos?part=id%2C%20contentDetails%2C%20snippet%2C%20status%2C%20statistics%2C%20liveStreamingDetails%2C%20localizations%2C%20player%2C%20recordingDetails%2C%20topicDetails%20&chart=mostPopular&maxResults=50&regionCode=US&key=[YOUR_API_KEY]'
\
--header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]'\
--header 'Accept: application/json'\
--compressed

# cURL Request Made for Page 2
curl \
'https://www.googleapis.com/youtube/v3/videos?part=id%2C%20contentDetails%2C%20snippet%2C%20status%2C%20statistics%2C%20liveStreamingDetails%2C%20localizations%2C%20player%2C%20recordingDetails%2C%20topicDetails%20&chart=mostPopular&maxResults=50&pageToken=CDIQAA&regionCode=US&key=[YOUR_API_KEY]'
\
--header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
--header 'Accept: application/json' \
--compressed

# cURL Request Made for Page 3
curl \
'https://www.googleapis.com/youtube/v3/videos?part=id%2C%20contentDetails%2C%20snippet%2C%20status%2C%20statistics%2C%20liveStreamingDetails%2C%20localizations%2C%20player%2C%20recordingDetails%2C%20topicDetails%20&chart=mostPopular&maxResults=50&pageToken=CGQQAA&regionCode=US&key=[YOUR_API_KEY]'
\
--header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
--header 'Accept: application/json' \
--compressed

# cURL Request Made for Page 4
curl \
'https://www.googleapis.com/youtube/v3/videos?part=id%2C%20contentDetails%2C%20snippet%2C%20status%2C%20statistics%2C%20liveStreamingDetails%2C%20localizations%2C%20player%2C%20recordingDetails%2C%20topicDetails%20&chart=mostPopular&maxResults=50&pageToken=CJYBEAA&regionCode=US&key=[YOUR_API_KEY]'
\
--header 'Accept: application/json' \
--compressed
