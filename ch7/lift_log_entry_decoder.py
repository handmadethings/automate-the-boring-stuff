# lift_log_entry_decoder
import re


# exercise, e.g. "2ct Squat"
exercise_regex = re.compile(r'([A-Za-z0-9 _.-]+):')

# Weight x reps, e.g. 120x5@8 (with or without kg/lb, with or without RPE rating)
weight_reps_rpe_regex = re.compile(r'(\d+)?[ ]*(kg|lb)?[ ]*x(\d+)[@]?(\d+)?')   

test_string_one = '2 ct squat: 120x12@8, 100x12@8, x10@9'

test_string_two = 'Deadlift: 120 kg x12@8, 100kg x12@8, 90 kgx10@9'

test_string_three = 'Muscle-ups: x12, x13, x9'

mo_one = exercise_regex.search(test_string_one)

mo_two = exercise_regex.search(test_string_two)

mo_three = exercise_regex.search(test_string_three)

print('Exercise found: ' + mo_one.group(1))
print('Exercise found: ' + mo_two.group(1))
print('Exercise found: ' + mo_three.group(1))

print(weight_reps_rpe_regex.findall(test_string_one))
print(weight_reps_rpe_regex.findall(test_string_two))
print(weight_reps_rpe_regex.findall(test_string_three))