from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer)

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'restaurant_domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):
					
	featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)
	agent = Agent(domain_file, policies = [MemoizationPolicy(max_history = 5), KerasPolicy(featurizer)])
	
	agent.train(
				training_data_file,
				#max_history = 3,
				epochs = 300,
				batch_size = 50,
				validation_split = 0.2,
				augmentation_factor = 50)
				
	agent.persist(model_path)
	return agent
	
def run_restaurant_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
	agent = Agent.load('./models/dialogue', interpreter = interpreter)
	
	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())
		
	return agent
	
if __name__ == '__main__':
	train_dialogue()
	run_restaurant_bot()
