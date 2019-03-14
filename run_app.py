from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-460632558514-460632558690-460834199909-6acce08bda67e872f7364b9b0b2dc119', #app verification token
							'xoxb-460632558514-462039209078-NXy1j6MsJ0mPj9U69qGIQUZ1', # bot verification token
							'7Bu15cPBawR4XYlpiWYk2xxQ', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))