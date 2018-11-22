from pprint import pprint

def policy2dnf(policies):

    dnf_policy = {}
    and_rules = []

    attributes = ["service", "resource", "action"]

    for role_and_permissions in policies: # [{role, permission}, ...]
        conditions = []
        for permission in role_and_permissions["permissions"]:
            for index, value in enumerate(permission.split(".")):

                condition = {}
                condition["attribute"] = attributes[index]
                condition["description"] = attributes[index] + "=" + value
                condition["operator"] = "="
                condition["type"] = "c"
                condition["value"] = value
                conditions.append(condition)

            condition = {}
            condition["attribute"] = "role"
            condition["description"] = "role" + "=" + role_and_permissions["role"]
            condition["operator"] = "="
            condition["type"] = "c"
            condition["value"] = role_and_permissions["role"]
            conditions.append(condition)

            rules = {}
            rules["conditions"] = conditions
            rules["description"] = role_and_permissions["role"]
            rules["enabled"] = True
            and_rules.append(rules)
            conditions = []

    dnf_policy["and_rules"] = and_rules

    pprint(dnf_policy)
    return dnf_policy


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
