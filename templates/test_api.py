import requests
import urllib.request
import os
import urllib.request
from PIL import Image


def download_image(url):
    save_dir = r'E:/Backend/ProTest/caches/'
    # Create the save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Construct the save path from the URL
    filename = os.path.basename(url)
    save_path = os.path.join(save_dir, filename)

    try:
        # Download image from URL
        urllib.request.urlretrieve(url, save_path)
    except urllib.error.HTTPError as e:
        print(f'Error downloading {url}: {e}')
        save_path = ''
    # save_path = "/" + save_path.replace("\\", "/")

    return save_path


req = requests.get("https://oracle.akam.uz/client/myresult?ticket_id=1130470")

json = req.json()['result'][0]['questions']
print(json)
for item in json:
    correct_ans = None
    if item['var_a_id'] == item['correct']:
        correct_ans = 1
    if item['var_b_id'] == item['correct']:
        correct_ans = 2
    if item['var_c_id'] == item['correct']:
        correct_ans = 3
    if item['var_d_id'] == item['correct']:
        correct_ans = 4
    elem = {
        'science': 1,
        'subject': 1,
        'question_name': item['question_name'] if item['question_name'] != ' ' else '',
        'akam_id': item['question_id'],
        'var_a_name': item['var_a_name'],
        # 'var_a_image': item['var_a_image'] if 'var_a_image' in item else None,
        'var_a_id': 1,
        'var_b_name': item['var_b_name'],
        # 'var_b_image': item['var_b_image'] if 'var_b_image' in item else None,
        'var_b_id': 2,
        'var_c_name': item['var_c_name'],
        # 'var_c_image': item['var_c_image'] if 'var_c_image' in item else None,
        'var_c_id': 3,
        'var_d_name': item['var_d_name'],
        # 'var_d_image': item['var_d_image'] if 'var_d_image' in item else None,
        'var_d_id': 4,
        'correct': correct_ans,
        'owner': 1
    }

    # files = {'question_image': download_image(item['image'])}
    if 'image' in item:
        image = download_image(item['image'])
        basename_img = os.path.basename(image)
        files = [
            ('question_image', (
                basename_img, open(image, 'rb'),
                'image/png'))
        ]
        headers = {
            'Content-Type': 'multipart/form-data; boundary=wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T',
            'Accept': '*/*',
        }
    else:
        files = None
        headers = {}

    print(files)
    res = requests.request('POST', "http://127.0.0.1:8000/api/v1/quizzes", headers=headers, data=elem, files=files)
    print(res.status_code)

    if files is not None:
        print(res.json())
