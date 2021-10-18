from flask import Flask, request, url_for, redirect
from markdown import markdown
from forex_python.converter import CurrencyRates, CurrencyCodes

msgTemplate = "<div style='font-weight: bold;color:red'>"
convert_MD_FileName="convert.md"
result_MD_FileName="exchangeResult.md"
app = Flask(__name__)

@app.route("/")
def homepage():

    return getReturnHtml("", convert_MD_FileName)

@app.route("/convert")
def vaild_fromcode_check():
    """
    Make sure all data are vaild
    convert code should be exist
    amount should be a postive floating number
    """
    covertFrom = request.args["covertfrom"].upper()
    covertTo = request.args["covertto"].upper()
    amount = request.args["amount"]

    errMsg= ""
    convertedAmount = None
    convertToSymbol = ""

    c = CurrencyRates()
    cc = CurrencyCodes()

    try:
        #judge covertFrom is valid currency code
        if covertFrom == "":
            errMsg += msgTemplate + "Not a vaild code: " + covertFrom + "</div>"

        c.get_rates(covertFrom)

    except:
        errMsg += msgTemplate + "Not a vaild code: " + covertFrom + "</div>"

    try:
        #judge convertTo is valid currency code
        if covertTo == "":
            errMsg += msgTemplate + "Not a vaild code: " + covertTo + "</div>"

        c.get_rates(covertTo)

    except:
        errMsg += msgTemplate + "Not a vaild code: " + covertTo + "</div>"


    #judge amount is a positive number
    try:
        if float(amount) < 0 :
            errMsg += msgTemplate + "Not a vaild amount: " + amount + "</div>"

    except:
        errMsg += msgTemplate + "Not a vaild amount: " + amount + "</div>"


    if errMsg != "":
        return getReturnHtml(errMsg, convert_MD_FileName)

    #Convert the currency
    try:
        convertedAmount = round(c.convert(covertFrom, covertTo, float(amount)),2)
        convertToSymbol = cc.get_symbol(covertTo)

    except:
        errMsg += msgTemplate + "Convert currency fail</div>"

    if errMsg != "":
        return getReturnHtml(errMsg, convert_MD_FileName)
    else:
        return redirect(url_for("result",convertedAmount=convertedAmount, convertToSymbol= convertToSymbol))

@app.route("/exchangeResult")
def result():
    """
    Add the reslt to the result page
    """
    convertToSymbol = request.args["convertToSymbol"]
    convertedAmount = request.args["convertedAmount"]

    return getReturnHtml("The result is " + convertToSymbol + convertedAmount , result_MD_FileName)


def getReturnHtml(frontText, fileName):
    with open(fileName, 'r') as f:
        text = f.read()
        html = markdown(frontText + text)
    return html
