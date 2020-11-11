#THIS IS A WEBSERVER FOR DEMONSTRATING THE TYPES OF RESPONSES WE SEE FROM AN API ENDPOINT
from flask import Flask
app = Flask(__name__)

#GET REQUEST

@app.route('/api/<string:food_name>')
def noAppId(food_name):
        message =  {'cod':'401','message':'Missing API key. Please see http://localhost:5000/faq#error401 for more info.'}
        return message

@app.route('/api/<string:food_name>/<string:appid>')
def getRequestHello(food_name, appid):
    appids = ['123', 'abc', 'top10', 'pythonking']
    store_request = {'123':[],'abc':[],'top10':[],'pythonking':[]}
    try:
        check_appid = appids[appids.index(appid)]
        store_request[check_appid].append('GET request for ' + str(food_name))
    except ValueError:
        server_response = {'cod':401, 'message':'Invalid API key. Please see http://localhost:5000/faq#error401 for more info.'}
        return server_response

    foods = ['apple', 'banna', 'mango', 'strawberries']
    colors = ['crimson', 'yellow', 'green', 'red']
    #answer = foods[foods.index(food_name)]
    #get user REQUEST
    food_facts = ["This can keep you from overeating. Eating fiber-rich foods helps control symptoms and lessens the effects of acid reflux. An apple's fiber can also help with diarrhea and constipation. Some studies show that plant chemicals and the fiber of an apple peel protect against blood vessel and heart damage","The best time to eat bananas depends on your nutritional needs and preference. Generally, the taste and nutritional value of bananas change as they ripen. Newly-ripened bananas tend to be less sweet than well-ripened bananas because the starch hasn't fully broken down into simple sugars","Mango is one of the sweetest fruits and lower in fiber than other fruits, so a good rule of thumb is not to exceed two servings a day. The United States Department of Agriculture recommends that adults eat 1 1/2 to 2 cups of fruit per day.","These potent little packages protect your heart, increase HDL (good) cholesterol, lower your blood pressure, and guard against cancer. Packed with vitamins, fiber, and particularly high levels of antioxidants known as polyphenols, strawberries are a sodium-free, fat-free, cholesterol-free, low-calorie food."]
    try:
        food_query = str(food_name.lower())
        food_index = foods.index(food_query)
        food_info  = str(food_facts[food_index])
        food_color = str(colors[food_index])
        answer = ""
        answer += "<!doctype html><html><head><title>Food API Info Page</title></head><body style='background-color:%s'>" % food_color
        answer += "<h1 style='text-align:center;color:black;'> %s (ID %i) </h1>" % (food_query,food_index)
        answer += "<p style='text-align:center;color:black'> %s </p></body></html>" % food_info
        return answer
    except ValueError:
        server_response = {'cod':401, 'message':'Food not Found In Our Cute API try Mango'}










#POST REQUEST
@app.route('/createHello', methods = ['POST'])
def postRequestHello():
	return "I see you sent a POST message :-)"
#UPDATE REQUEST
@app.route('/updateHello', methods = ['PUT'])
def updateRequestHello():
	return "Sending Hello on an PUT request!"

#DELETE REQUEST
@app.route('/deleteHello', methods = ['DELETE'])
def deleteRequestHello():
	return "Deleting your hard drive.....haha just kidding! I received a DELETE request!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
