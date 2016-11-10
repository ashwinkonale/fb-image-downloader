import json
import urllib

ALBUM_ID = "1315007841865494"
PAGINATION_URL = "https://graph.facebook.com/v2.8/1315007841865494?fields=photos.limit(1)&access_token=EAACEdEose0cBAANQYB84n7wLZCPNGehXOi9ZCJfSK8zSBr0LCKjGGrSCojpCCkD0ISBPPwWiHbJPeI8F6DfC2X9001po5pn3cM4JXecbvefFNuLzG1XOk9n3r2bBvX2ou1zs3a3qNSEaqzOu8PLkaN1ZBktTZA9HhtsSafthCAZDZD"
ALL_IMAGE_LINKS_URL = "https://graph.facebook.com/v2.8/%s?fields=webp_images&access_token=EAACEdEose0cBAANQYB84n7wLZCPNGehXOi9ZCJfSK8zSBr0LCKjGGrSCojpCCkD0ISBPPwWiHbJPeI8F6DfC2X9001po5pn3cM4JXecbvefFNuLzG1XOk9n3r2bBvX2ou1zs3a3qNSEaqzOu8PLkaN1ZBktTZA9HhtsSafthCAZDZD"

def download_image(url, img_id):
    print "Downloading %s"%image_id
    urllib.urlretrieve(url, "%s.jpg" % img_id)


def get_image_id(pagination_url, first = False):
    data = urllib.urlopen(pagination_url)
    image_data = json.loads(data.read())
    if(first):
        image_id = image_data.get("photos").get("data")[0]["id"]
        next_image = image_data.get("photos").get("paging").get("next")
    else:
        image_id = image_data.get("data")[0]["id"]
        next_image = image_data.get("paging").get("next")
    return image_id, next_image

def get_full_resolution_image_url(image_id):
    data = urllib.urlopen(ALL_IMAGE_LINKS_URL%str(image_id))
    all_images = json.loads(data.read())
    full_length_image_url = all_images.get("webp_images")[0]["source"]
    full_length_image_url = full_length_image_url.replace(".webp", "")
    download_image(full_length_image_url,  image_id)

if __name__ == "__main__":
    counter = 0
    image_id = ""
    next_image = ""
    image_id, next_image = get_image_id(PAGINATION_URL, True)
    while next_image!=None:
        get_full_resolution_image_url(image_id)
        counter+=1
        image_id, next_image = get_image_id(next_image)

    get_full_resolution_image_url(image_id)
    print "Thank you"
