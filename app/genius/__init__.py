class API:
    
    def __init__(self, access_token):
        '''
        Constructor for API object
        '''
        self._access_token = 'Bearer {}'.format(access_token)
        self.api_root = 'https://api.genius.com/'
    
    def _make_request(self, path, method='GET'):
        '''
        Make request to API
        '''
        try:
            _url = self.api_root+path
            if method == 'GET':
                response = requests.get(_url, headers={'Authorization': self._access_token})
            return True, response.json()
        
        except Exception as  error:
            return False, None
        
    def sanitize_songs(self, results):
        '''
        Cleans the songs returned by Genius
        '''
        songs = []
        for result in results:
    
            data = result['result']
            song = (data['id'],data['title'],)
            songs.append(song)
            
        return songs
    
    def search_artist(self, query, max_songs=10):
        '''
        Search for artist
        '''
        try:
            query = '%20'.join(query.split(' '))
            path = 'search?q='+query
            valid, response = self._make_request(path)
            if valid:
                
                artist_data = response['response']['hits'][0]['result']['primary_artist']
                results = response['response']['hits']
                
            else:
                return None
            
            _songs = self.sanitize_songs(results)
            
            artist = Artist(artist_data['id'],artist_data['name'],artist_data['image_url'], _songs)
            return artist
            
        except Exception as error:
            
            return None