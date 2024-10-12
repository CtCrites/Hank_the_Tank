from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
 

import os

def Convoloop(user_name):
	os.environ["OPENAI_API_KEY"] = open_ai_key
	ind = "on"
	while ind == "on":
		user_input = input("{}: ".format(user_name))
		
		if user_input == "x" or user_input == "X":
			ind = "off"
			break
		elif "your" in user_input and "name" in user_input:
			P = 1
		elif "my" in user_input and "name" in user_input:
			P = 2
		else:
			P = 3
		
		match P:
			case 1:
				prompt = PromptTemplate(
					input_variables=["concept"],
					template="Respond to {concept} as if you were a man named Hank",
				)
				llm = OpenAI(temperature=1.4)
				chain = LLMChain(llm=llm, prompt=prompt)
				output = chain.run(user_input)
				output = output[2::]
				print("HANK: " + output)	
			case 2:
				temp = "Respond to {concept} as if my name is " + user_name
				prompt = PromptTemplate(
					input_variables=["concept"],
					template=temp,
				)
				llm = OpenAI(temperature=1.4)
				chain = LLMChain(llm=llm, prompt=prompt)
				output = chain.run(user_input)
				output = output[2::]
				print("HANK: " + output)
			case 3:
				prompt = PromptTemplate(
					input_variables=["concept"],
					template="Respond creatively to {concept}",
				)
				llm = OpenAI(temperature=1.4)
				chain = LLMChain(llm=llm, prompt=prompt)
				output = chain.run(user_input)
				output = output[2::]
				print("HANK: " + output)
				
	return output

Convoloop("Cameron")
#Change the prompt template using a switch case statement
#Have each case being a prior knowledge trail
