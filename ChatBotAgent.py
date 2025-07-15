import re
from ResearchAgent import ResearchAgent
from random_responses import random_string

class ChatBotAgent:
    def __init__(self):
        # Initialize the research agent for data queries
        self.research_agent = ResearchAgent()
        
    def greet_user(self):
        """Display welcome message and available help options"""
        print("=" * 50)
        print("🍵 Welcome to SmartCafe Assistant! 🍵")
        print("=" * 50)
        print("I'm here to help you with information about our cafe!")
        print("\nYou can ask me about:")
        print("- Menu items and ingredients")
        print("- Prices of drinks")
        print("- Nutritional information")
        print("- Our opening hours")
        print("- Available drinks")
        print("\nType 'exit' or 'quit' to end the conversation.")
        print("-" * 50)
    
    def detect_intent(self, user_input):
        """Use regex to detect user intent and route to appropriate response"""
        user_input_lower = user_input.lower()
        
        # Intent patterns using regex
        price_patterns = [r'\b(price|cost|how much|expensive)\b', r'\$']
        ingredient_patterns = [r'\b(ingredient|made of|contains|what.*in)\b']
        nutrition_patterns = [r'\b(calorie|nutrition|sugar|healthy|fat)\b']
        hours_patterns = [r'\b(hour|open|close|time|when)\b']
        menu_patterns = [r'\b(menu|drink|beverage|what.*have|available|offer)\b']
        
        # Check for exit commands
        if re.search(r'\b(exit|quit|bye|goodbye)\b', user_input_lower):
            return 'exit'
        
        # Check each intent pattern
        if any(re.search(pattern, user_input_lower) for pattern in price_patterns):
            return 'price'
        elif any(re.search(pattern, user_input_lower) for pattern in ingredient_patterns):
            return 'ingredients'
        elif any(re.search(pattern, user_input_lower) for pattern in nutrition_patterns):
            return 'nutrition'
        elif any(re.search(pattern, user_input_lower) for pattern in hours_patterns):
            return 'hours'
        elif any(re.search(pattern, user_input_lower) for pattern in menu_patterns):
            return 'menu'
        else:
            return 'unknown'
    
    def route_response(self, user_input, intent):
        """Route the user input to the appropriate ResearchAgent method based on intent"""
        try:
            if intent == 'price':
                return self.research_agent.get_price(user_input)
            elif intent == 'ingredients':
                return self.research_agent.get_ingredients(user_input)
            elif intent == 'nutrition':
                return self.research_agent.get_nutrition(user_input)
            elif intent == 'hours':
                return self.research_agent.get_hours(user_input)
            elif intent == 'menu':
                return self.research_agent.list_drinks()
            elif intent == 'unknown':
                return random_string()
            else:
                return "I'm not sure how to help with that. Please try rephrasing your question."
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def start_conversation(self):
        """Main conversation loop"""
        self.greet_user()
        
        while True:
            try:
                # Get user input
                user_input = input("\n🤔 You: ").strip()
                
                # Check if user wants to exit
                if not user_input:
                    print("🤖 Bot: Please type something or 'exit' to quit.")
                    continue
                
                # Detect intent using regex
                intent = self.detect_intent(user_input)
                
                # Handle exit
                if intent == 'exit':
                    print("🤖 Bot: Thank you for visiting SmartCafe! Have a great day! ☕")
                    break
                
                # Get response from research agent
                response = self.route_response(user_input, intent)
                print(f"🤖 Bot: {response}")
                
            except KeyboardInterrupt:
                print("\n🤖 Bot: Goodbye! Thanks for using SmartCafe Assistant! ☕")
                break
            except Exception as e:
                print(f"🤖 Bot: Sorry, something went wrong: {str(e)}")
