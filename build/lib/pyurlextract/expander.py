import requests

def extract_shorturl(short_url):
    try:
        response = requests.get(short_url, allow_redirects=False)
        
        # All redirection links
        redirection_links = []

        # Follow redirections
        while 'Location' in response.headers:
            redirect_url = response.headers['Location']
            redirection_links.append(redirect_url)
            response = requests.get(redirect_url, allow_redirects=False)

        final_link = response.url
        redirection_links.append(final_link)
        
        return final_link, redirection_links

    except requests.exceptions.RequestException as e:
        return None, [f"Error fetching the URL: {e}"]