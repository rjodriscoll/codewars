def generate_hashtag(s):
    
    if len(s) < 1:
        return False
    
    else:
        split_words = s.split()
        split_words = [w.lower().capitalize() for w in split_words]
        split_words.insert( 0,'#')
        hashtag = ''.join(split_words)
        
        

        if len(hashtag) > 140:
            return False
        else:
            return hashtag