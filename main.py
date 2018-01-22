from facepy import GraphAPI
from datetime import date
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\mihai\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
# print(pytesseract.image_to_string(Image.open('C:\\Users\\mihai\\Desktop\\ayo.jpg')))


token = "EAACEdEose0cBAHfZCNhFfZBxJLq2TabI4n5VUUZCiOg91bsQ3GXQutfZBoJ9VycFiDpc9t3kQuTOAj18goPgEyLwEGBzvTsoDAY7arj7t0DmUwRWf2S1yRuZCko2XxuSRnzLOyBzsU7OziOrP5grPu72nTVoUxUDZCxdd9a5LBfWkzRZBIGJ1ctT5YKeAWBQZALaHeVv6z0SLUm9n0x1IrJyNYNcNGd3kh8ZD"
graph = GraphAPI(token)


def get_timeline_album_id():
    albums = graph.get("AYOrestaurant/albums")
    for album in albums.get("data"):
        if album.get("name") == "Timeline Photos":
            return album.get("id")

def get_today_timeline_photo_ids():
    today_photos = []
    timeline_photos = graph.get(get_timeline_album_id() + "/photos").get("data")
    for photo in timeline_photos:
        if(str(date.today()) in photo.get("created_time")):
            today_photos.append(photo.get("id"))
    return today_photos

def get_today_post_ids():
    all_posts = graph.get("AYOrestaurant/posts").get("data")
    today_posts = []
    for post in all_posts:
        if (str(date.today()) in post.get("created_time")):
            today_posts.append(post.get("id"))
    return today_posts

def get_today_post_picture_urls():
    picture_urls = []
    for post in get_today_post_ids():
        picture_urls.append(graph.get(post + "?fields=full_picture").get("full_picture"))
    return picture_urls


def get_today_picture_urls():
    picture_urls = []
    for post in get_today_timeline_photo_ids():
        picture_urls.append(graph.get(post + "/picture?type=normal&redirect=false").get("data").get("url"))
    return picture_urls

print(get_today_picture_urls())