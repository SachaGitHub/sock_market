from bs4 import *
import requests

class api:
    def __init__(self):
        pass
    def action(company):
        link = "https://finance.yahoo.com/quote/"+company +"?p=" + company
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            action = soup.select_one('span[class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]').text
            return action
        except:
            return "Error to get action of " + company
    def action_selled(company):
        link = "https://finance.yahoo.com/quote/"+company +"?p=" + company
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            action_selled =  soup.select_one('span[class="Trsdu(0.3s)"]').text
            return action_selled
        except:
            return "Error to get action selled of " + company
    def statistics(company):
        link = "https://finance.yahoo.com/quote/"+company +"?p=" + company
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            statistics =  soup.select_one('span[class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"]').text
            statistics = statistics.split(" ")
            return statistics[0]
        except:
            return "Error to get statistics of " + company
    def statistics_pourcentage(company):
        link = "https://finance.yahoo.com/quote/"+company +"?p=" + company
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            statistics =  soup.select_one('span[class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"]').text
            statistics = statistics.split(" ")
            return statistics[1]
        except:
            return "Error to get statistics of " + company
    def all(company):
        link = "https://finance.yahoo.com/quote/"+company +"?p=" + company
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            statistics =  soup.select_one('span[class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"]').text
            statistics = statistics.split(" ")
            action_selled =  soup.select_one('span[class="Trsdu(0.3s)"]').text
            action = soup.select_one('span[class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]').text
            return "stats " + statistics[0] + " stats " + statistics[1] + " action selled : " + action_selled + " action price : " + action
        except:
            return "Error to get all of " + company