#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)    # Store comics in ./xkcd

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print(f'Downloading page https://xkcd.com/{url_number}...')
        res = requests.get('https://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL for the comic image.
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image.
            print('Downloading image {comic_url}...')
            res = requests.get('https:' + comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')

            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

# TODO: Create and start the Thread objects.
# TODO: Wait for all threads to end.
