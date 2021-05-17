from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
#    return "<img src=https://post-phinf.pstatic.net/MjAxOTEyMzFfMTQz/MDAxNTc3NzU4NjE3ODE5.hyQQVHg1LCrJ1Y_J1NPfFIXFt8PXajxhLVxiV2ImdPcg.cHN_veuJwQcRzE8oHOfxjlz_AUXds5sRFrDRBtaEMQ0g.JPEG/%ED%8E%AD%EC%88%98%ED%95%98.jpg?type=w1200>"
    return_value=""
    image_value="https://post-phinf.pstatic.net/MjAxOTEyMzFfMTQz/MDAxNTc3NzU4NjE3ODE5.hyQQVHg1LCrJ1Y_J1NPfFIXFt8PXajxhLVxiV2ImdPcg.cHN_veuJwQcRzE8oHOfxjlz_AUXds5sRFrDRBtaEMQ0g.JPEG/%ED%8E%AD%EC%88%98%ED%95%98.jpg?type=w1200"
    return_value="<img src=\""+image_value+"\">"
    print(return_value)
    return return_value
@app.route('/downfile/woowahan')
def down_woowahan():
    file_woowahan='/home/ec2-user/uwsgi_server/download/woowahan.zip'
    return file_woowahan
 

if __name__ == "__main__":
    application.run(host='0.0.0.0')
