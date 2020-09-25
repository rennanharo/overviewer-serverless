import pandas as pd
import json
import csv
import datetime as dt

# Call functions to populate the dictionary
def clean_json(tag):
    with open(f'miner/assets/temp/instagram/{tag}.json') as file:
        data = json.load(file)
    file.close()
    
    posts = range(len(data['GraphImages']))
    
    filtered = {
    'likes': [],
    'captions': [],
    'comments': [],
    'timestamp': [],
    'is_video': [],
    'tags': []
    }
    
    # Get likes
    def get_likes(data, posts):
        for post in posts:
            edge_liked_by = data['GraphImages'][post]['edge_liked_by']
            for item in edge_liked_by.values():
                filtered['likes'].append(item)

    # Get captions
    def get_captions(data, posts):
        for post in posts:
            edge_media_to_caption = data['GraphImages'][post]['edge_media_to_caption']['edges'][0]['node']
            for item in edge_media_to_caption.values():
                filtered['captions'].append(item)

    # Get comments
    def get_comments(data, posts):
        for post in posts:
            media_comment = data['GraphImages'][post]['edge_media_to_comment']['data']
            posts_range = range(len(data['GraphImages'][post]['edge_media_to_comment']['data']))
            post_comments = []
            for comment in posts_range:
                post_comments.append(media_comment[comment]['text'])
            filtered['comments'].append(post_comments)       

    # Get is_video
    def get_is_video(data, posts):
        for post in posts:
            is_video = data['GraphImages'][post]['is_video']
            filtered['is_video'].append(is_video)

    # Get tags
    def get_tags(data, posts):
        for post in posts:
            tags = data['GraphImages'][post]['tags']
            filtered['tags'].append(tags)

    # Get timestamps
    def get_timestamps(data, posts):
        for post in posts:
            timestamp = dt.datetime.fromtimestamp(data['GraphImages'][post]['taken_at_timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            filtered['timestamp'].append(timestamp)

    get_likes(data, posts)
    get_captions(data, posts)
    get_comments(data, posts)
    get_is_video(data, posts)
    get_tags(data, posts)
    get_timestamps(data, posts)

    # Convert dictionary into dataframe
    df = pd.DataFrame.from_dict(filtered)
    df['comments'] = df['comments'].str.join("','")
    df['tags'] = df['tags'].str.join("','")
    df = df.sort_values(by = 'likes', ascending = False)
    return df

    