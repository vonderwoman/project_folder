import gradio as gr
import requests
from stock_price_node import StockPriceNode
from investment_node import InvestmentNode
from supervisor_node import SupervisorNode
from conversation_node import ConversationNode

# Initialize specialized nodes
stock_price_node = StockPriceNode()
investment_node = InvestmentNode()
supervisor_node = SupervisorNode()
conversation_node = ConversationNode()

# Yahoo Finance API key
rapidapi_key = ''

# Function to handle user input and generate response
def handle_user_input(user_input):
    # Route user input to appropriate node
    next_node = supervisor_node.route_to_next_node(user_input)

    # Handle conversation based on the selected node
    if next_node == "stock_price":
        stock_symbol = user_input
        # Modify the method call to provide only two arguments
        stock_price = stock_price_node.get_stock_price(stock_symbol)
        response = f"The current price of {stock_symbol} is ${stock_price}"

    elif next_node == "investment":
        investment_amount = float(user_input)
        recommendation = investment_node.get_recommendation(investment_amount)
        response = recommendation

    elif next_node == "conversation":
        response = conversation_node.handle_general_query(user_input)

    # Check if conversation should end
    if next_node == "FINISH":
        return "Conversation finished."
    
    return response

# Create Gradio interface
gr.Interface(fn=handle_user_input, inputs="textbox", outputs="textbox").launch()