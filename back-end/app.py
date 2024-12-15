from flask import Flask, render_template, request, send_from_directory
from glob import glob
import os

app = Flask(__name__, template_folder="../front-end/templates")

IMG_PATH = "D:\\img"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/main")
def main():
    return render_template('main.html')


@app.route('/test')
def test():
    return render_template('test.html')

@app.route("/retrieve", methods=["GET", "POST"])
def retrieve():
    query = None

    if request.method == 'POST':
        query = request.form.get('query')  # Lấy giá trị từ form
        # Tìm kiếm từ dữ liệu mẫu
        
    return render_template('retrieve.html', query=query)

@app.route("/gallery")
def gallery():
    img_files = os.path.join("D:\\img", "*.jpg")
    imgs = glob(img_files)
    for i in range(len(imgs)):
        img = imgs[i]
        img = os.path.basename(img)
        imgs[i] = img        
    return render_template("gallery.html", imgs=imgs)

# Route để phục vụ tệp ảnh từ thư mục bên ngoài
@app.route('/external-images/<filename>')
def external_images(filename):
    return send_from_directory(IMG_PATH, filename)

if __name__ == "__main__":
    # print(app.config)
    app.run(debug=True)
