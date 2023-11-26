from flask import Flask, render_template, request
import main

db = main.get_db()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        option1 = request.form.get("option1") # Day of week
        option2 = request.form.get("option2") # Class time 
        option3 = request.form.get("option3", default=1, type=int) # Week number

        data = main.query(db, option2, option1, option3)
        print(option1, option2, option3, data)
        
        params = {
            "option1": option1,
            "option2": option2,
            "option3": str(option3),
            "data": data,
            "weekOptions": [["7",'7(10.9-10.15)'], ["8",'8(10.16-10.22)'], ["9",'9(10.23-10.29)'], ["10",'10(10.30-11.5)'], ["11",'11(11.6-11.12)'],["12",'12(11.13-11.19)'], ["13",'13(11.20-11.26)'], ["14",'14(11.27-12.3)'], ["15",'15(12.4-12.10)'], ["16",'16(12.11-12.17)'], ["17",'17(12.18-12.24)'], ["18",'18(12.25-12.31)'], ["19",'19(1.1-1.7)']],
            "dayOptions" : ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"],
            "timeOptions": [["第一二节",'第1-2节(8:20-10:00)'], ["第三四节",'第3-4节(10:20-12:00)'], ["第五六节",'第5-6节(14:00-15:40)'], ["第七八节",'第7-8节(16:00-17:40)'], ["第九十节",'第9-10节(18:30-20:00)']]
        }
        return render_template("./index.html", **params)

    params = {
        "weekOptions": [["7",'7(10.9-10.15)'], ["8",'8(10.16-10.22)'], ["9",'9(10.23-10.29)'], ["10",'10(10.30-11.5)'], ["11",'11(11.6-11.12)'],["12",'12(11.13-11.19)'], ["13",'13(11.20-11.26)'], ["14",'14(11.27-12.3)'], ["15",'15(12.4-12.10)'], ["16",'16(12.11-12.17)'], ["17",'17(12.18-12.24)'], ["18",'18(12.25-12.31)'], ["19",'19(1.1-1.7)']],
        "dayOptions" : ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"],
        "timeOptions": [["第一二节",'第1-2节(8:20-10:00)'], ["第三四节",'第3-4节(10:20-12:00)'], ["第五六节",'第5-6节(14:00-15:40)'], ["第七八节",'第7-8节(16:00-17:40)'], ["第九十节",'第9-10节(18:30-20:00)']]
    }
    return render_template("index.html", **params)