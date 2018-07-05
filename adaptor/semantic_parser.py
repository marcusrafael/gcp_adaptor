from pprint import pprint

def policy2local(policies):
    final = []
    policy = {}
    for conditions in policies["dnf_policy"]["and_rules"]:
        pprint(conditions)
        permission = ""
        for condition in conditions["conditions"]:
            value = condition["value"]
            if (permission.count(".") < 2):
                permission = permission + value + "."
            elif ("/" not in value):
                permission = permission + value
            elif ("/" in value):
                role = value
        if not role in policy:
            policy[role] = []
        policy[role].append(permission)
    for key in policy:
        final.append({"role": key, "permissions": policy[key]})
    pprint(final)
    return final
