# updating and resizing account picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125, 125)
    resized_pic = Image.open(form_picture)
    resized_pic.thumbnail(output_size)
    resized_pic.save(picture_path)
    return picture_fn