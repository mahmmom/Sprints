import json
import re

class ResearchAgent():
    def __init__(self):
        with open("cafe_data.json") as f:
            self.data = json.load(f)

    def list_drinks(self):
        return "Here are the drinks we offer:\n- " + "\n- ".join(self.data["drinks"])
    
    def list_opening_hours(self):
        hours = []
        for day, time in self.data["opening_hours"].items():
            hours.append(f"{day}: {time}")
        return "\n".join(hours)

    def get_price(self, user_input):
        for drink in self.data["menu"]:
            if re.search(drink, user_input, re.IGNORECASE):
                return f"The price of {drink} is ${self.data['menu'][drink]['price_usd']:.2f}"
        return "Sorry, I couldn't find that drink on the menu."

    def get_ingredients(self, user_input):
        for drink in self.data["menu"]:
            if re.search(drink, user_input, re.IGNORECASE):
                ingredients = ", ".join(self.data["menu"][drink]["ingredients"])
                return f"The ingredients in {drink} are: {ingredients}."
        return "I'm not sure which drink you're asking about."
    
    def get_nutrition(self, user_input):
        for drink in self.data["menu"]:
            if re.search(drink, user_input, re.IGNORECASE):
                nutrition = self.data["menu"][drink]["nutrition"]
                return f"The nutrition facts for {drink} are: {nutrition}."
        return "I’m not sure which drink you're asking about."
    
    def get_hours(self, user_input):
        for day in self.data["opening_hours"]:
            if re.search(day, user_input, re.IGNORECASE):
                return f"Our hours on {day} are: {self.data['opening_hours'][day]}"
        return "We’re open every day! Want to ask about a specific day?"
    

    

agent = ResearchAgent()

print(agent.get_price("Mocha Caramel Latte price?"))
print(agent.get_ingredients("What are the ingredients in Caramel Latte?"))
print(agent.get_hours("What are your hours on Saturday?"))  
print(agent.list_drinks())

