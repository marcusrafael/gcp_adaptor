from pprint import pprint

def policy2dnf(policy):

    dnf_policy = {}
    and_rules = []

    attributes = ["service", "resource", "action"]

    for role_and_permissions in policy: # [{role, permission}, ...]
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


def policy2local(dnf_policy):
    policy = []
    role_permissions_mapping = {}
    for rule in dnf_policy["and_rules"]:
        permission = {}
        for condition in rule["conditions"]:
            permission[condition["attribute"]] = condition["value"]

        formated_permission = "{0}.{1}.{2}".format(permission["service"],
                                                   permission["resource"],
                                                   permission["action"])
        role = permission["role"]
        if role in role_permissions_mapping:
            role_permissions_mapping[role].append(formated_permission)
        else:
            role_permissions_mapping[role] = [formated_permission]

    for role in role_permissions_mapping.keys():
        policy.append({"role": role, "permissions": role_permissions_mapping[role]})

    return policy
