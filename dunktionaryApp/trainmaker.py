import random
from django.shortcuts import render
from .models import PassLevel, DunkLevel, TrickScore


class TrickWrapper:
	def __init__(self, db_obj, is_pass=True):
		if is_pass:
			self.name = db_obj.pass_ref.name
			self.can_start = db_obj.can_start
			self.can_follow = db_obj.can_follow
		else:
			self.name = db_obj.dunk_ref.name
			self.can_start = False
			self.can_follow = False
		
		self.level = db_obj.level
		self.variations = [v.name for v in db_obj.variations.all()]
		
	def get_random_variation(self):
		return random.choice(self.variations) if self.variations else self.name

def make_a_train(num_people, level):
	valid_passes = [
		TrickWrapper(p, is_pass=True) 
		for p in PassLevel.objects.filter(
			level__lte=level
		).select_related('pass_ref').prefetch_related('variations')
	]
	valid_dunks = [
		TrickWrapper(d, is_pass=False) 
		for d in DunkLevel.objects.filter(
			level__lte=level
		).select_related('dunk_ref').prefetch_related('variations')
	]
		
	if not valid_passes:
		print("No valid passes for the specified level.")
		return [], 0
		
	if not valid_dunks:
		print("No valid dunks for the specified level.")
		return [], 0
		
	train = []
	total_score = 0
		
	# Get scores from database (cache in dict for performance)
	scores_dict = dict(TrickScore.objects.values_list('trick_name', 'score_value'))
		
	random.shuffle(valid_passes)
	random.shuffle(valid_dunks)
		
	# Assign start pass to the first person
	start_passes = [p for p in valid_passes if p.can_start]
	if not start_passes:
		print("No valid start passes for the specified level.")
		return [], 0
		
	start_pass = random.choice(start_passes)
		
	# Check if there are variations available for the start
	if start_pass.variations:
		variation_probability = min(1.0, 0.5 + (level - start_pass.level) * 0.25)
		if random.random() < variation_probability:
			variation = random.choice(start_pass.variations)
			train.append(f"{variation} - {start_pass.name}")
			total_score += scores_dict.get(f"{variation} {start_pass.name}", 0)
		else:
			train.append(start_pass.name)
			total_score += scores_dict.get(start_pass.name, 0)
	else:
		train.append(start_pass.name)
		total_score += scores_dict.get(start_pass.name, 0)
		
	# Assign follow passes to the rest of the people
	for i in range(2, num_people):
		pass_ = random.choice(valid_passes)
		
		# Check if there are variations available for the pass
		if pass_.variations:
			variation_probability = min(1.0, 0.5 + (level - pass_.level) * 0.20)
			if random.random() < variation_probability:
				variation = pass_.get_random_variation()
				train.append(f"{variation} - {pass_.name}")
				total_score += scores_dict.get(f"{variation} {pass_.name}", 0) + 0.1
			else:
				train.append(pass_.name)
				total_score += scores_dict.get(pass_.name, 0) + 0.1
		else:
			train.append(pass_.name)
			total_score += scores_dict.get(pass_.name, 0) + 0.1
		
	# Assign dunk to the dunker
	dunk = random.choice(valid_dunks)
		
	# Check if there are variations available for the dunk
	if dunk.variations:
		variation_probability = min(1.0, 0.65 + (level - dunk.level) * 0.3)
		if random.random() < variation_probability:
			variation = dunk.get_random_variation()
			train.append(f"{variation} - {dunk.name}")
			total_score += scores_dict.get(f"{variation} {dunk.name}", 0) + 0.1
		else:
			train.append(dunk.name)
			total_score += scores_dict.get(dunk.name, 0) + 0.1
	else:
		train.append(dunk.name)
		total_score += scores_dict.get(dunk.name, 0) + 0.1
		
	return train, total_score

def custom_train(custom_train_names):
    scores_dict = dict(TrickScore.objects.values_list('trick_name', 'score_value'))
    total_score = 0
    not_found_passes = []
    
    for pass_name in custom_train_names:
        score = scores_dict.get(pass_name)
        if score is not None:
            total_score += score
        else:
            not_found_passes.append(pass_name)
    
    return total_score, not_found_passes

# How to read what trick was before and make sure you can't always follow, ex. barani bounce after BTB
# add 2 vs 1 trampoline functions, cross off the glass, cross baranis
# Add lay down float, OTB float, ball holds etc
