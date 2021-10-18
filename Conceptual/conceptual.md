### Conceptual Exercise

####Answer the following questions below:

#####- What are important differences between Python and JavaScript?  
 Python is a scripting language used for developing both desktop and web applications. JavaScript is a client side scripting language.
#####- In python, when the function is called with wrong parameters, error will raise. In JavaScript, it does not care about the functions are called with correct parameters or not.Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways youcan try to get a missing key (like "c") *without* your programmingcrashing.
	1. Using get() to check if the key exists, if not return.
	2. Using setdefault() to check if the key exists, if not, create the key.
#####- What is a unit test?
It's a way of testing small piece of code. It's can check each function if it works.
#####- What is an integration test?
Integration testing is the phase in software testing in which individual software modules are combined and tested as a group.

#####- What is the role of web application framework, like Flask?
It's designed to support the development of web applications including web services, web resources, and web APIs.

#####- You can pass information to Flask either as a parameter in a route URL(like '/foods/pretzel') or using a URL query param (like'foods?type=pretzel'). How might you choose which one is a better fitfor an application?
If need to represent the current page information. I will use URL query param. In addition, route URL is Common use.  
#####- How do you collect data from a URL placeholder parameter using Flask?
use request.args.get to collect the data from a URL placeholder parameter.
#####- How do you collect data from the query string using Flask?
use request.args to collect the data.
#####- How do you collect data from the body of the request using Flask?
use request.form to collect the data.
#####- What is a cookie and what kinds of things are they commonly used for?
Cookies are essential to the modern Internet but a vulnerability to privacy. Cookies help web developers give more personal, convenient website visits. Cookies commonly used like a username and password — that are used to identify your computer as you use a computer network.
#####- What is the session object in Flask?
Session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.
#####- What does Flask's `jsonify()` do?
It is a helper method provided by Flask to properly return JSON data.