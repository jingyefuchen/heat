# -*-coding:utf-8-*-

import web
import requests

urls = ("/", "index",
        "/add", "add")
render = web.template.render("templates/")

def request_get(word):
    key = "d99936156f33eb2a11ba6545ba7182b4"
    url = "http://api.tianapi.com/txapi/nutrient/index?key=%s&word=%s&mode=0" % (key, word)
    ret = requests.get(url=url)
    content = eval(ret.content)
    if content.get("code") == 200:
        return content.get("newslist")[0].get("rl")

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
        allheat = heat
        for i in range(1, 12):
            food_name = "food" + str(i)
            food = data.get(food_name)
            food_weight = food_name + "_weight"
            foodWeight = data.get(food_weight)
            if food and foodWeight:
                createHeat = float(request_get(food)) * float(foodWeight) / 100
                allheat = allheat - createHeat

        return "your base heat is %s" % -allheat




if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
