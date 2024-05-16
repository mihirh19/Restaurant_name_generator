import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm = ChatCohere()
def generate_restaurant_name_and_items(cusine):

   
   prompt_template_name = PromptTemplate(
      input_variables=['cuisine'],
      template="I want to open restaurant for {cuisine} food. suggest a fency name for this.give only one name."
      
   )
   name_chain= LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
   
   prompt_template_item = PromptTemplate(
      input_variables=['restaurant_name'],
      template="Suggest Some menu items for {restaurant_name}."
   )
   # prompt_template_item = ChatPromptTemplate.from_template("Suggest Some menu items for {restaurant_name}.")
   food_item_chain = LLMChain(llm=llm, prompt=prompt_template_item, output_key="menu_items")
   
   # chain = SequentialChain(chains=[name_chain, food_item_chain],
   #                input_variables=['cuisine'],
   #                output_variables=['restaurant_name', 'menu_items']
   #       )
   chain = name_chain | food_item_chain
   responce = chain.invoke({"cuisine":cusine})
   return responce 
   

if __name__ == '__main__': 
   print(generate_restaurant_name_and_items("Indian"))
