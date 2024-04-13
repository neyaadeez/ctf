import hashlib
username = b"GOUGH"
key_part_dynamic1_trial = []
hexdigest = hashlib.sha256(username)
values = [4, 5, 3, 6, 2, 7, 1, 8]
for k in values:
    key_part_dynamic1_trial.append(hexdigest.hexdigest()[k])

st = ''.join(key_part_dynamic1_trial)
print(st)
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = st
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)
