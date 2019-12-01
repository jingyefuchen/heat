# -*-coding:utf-8-*-

import web

def main():
    sex = input("input your sex(F/M):")
    weight = float(input("input your weight(kg):"))
    height = float(input("input your height(cm):"))
    age = float(input("input your age(year):"))
    if sex == "M":
        heat = 66 + 13.7 * weight + 5 * height - 6.8 * age
    else:
        heat = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
    print ("your base heat is %s" % heat)

urls = ("/", "index",
        "/add", "add")
render = web.template.render("templates/")

class index():
    def GET(self):
        return render.index()

    def POST(self):
        data = web.input()
        sex = data.get("sex")
        weight = float(data.get("weight"))
        height = float(data.get("height"))
        age = float(data.get("age"))
        if sex == "M":
            heat = 66 + 13.7 * weight + 5 * height - 6.8 * age
        else:
            heat = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
        return "your base heat is %s" % heat

class add():
    def GET(self):
        return "hello,world!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
