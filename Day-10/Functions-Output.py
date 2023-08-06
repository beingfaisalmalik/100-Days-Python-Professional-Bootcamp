def formt_name(first_name, last_name):
    if first_name and last_name:
        return first_name.title() +" "+ last_name.title()
    elif first_name:
        return first_name.lower()
    elif last_name:
        return last_name.lower()
    else:
        return None
name = formt_name('faisal','malik')
print(name)