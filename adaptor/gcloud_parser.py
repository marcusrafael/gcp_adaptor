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
    if 'and_rules' in dnf_policy: # If there is no and_rules, just return an empty policy
        for and_rule in dnf_policy['and_rules']: # For each and_rule
            enabled = True
            if 'enabled' in and_rule:
                enabled = and_rule['enabled']
            if enabled:  # If it is enabled
                role = ""
                service = ""
                resource = ""
                action  = ""
                for cond in and_rule['conditions']: # Check all Conditions
                    print(cond)
                    if 'attribute' in cond:
                        if cond['attribute'] == "role":    # Retrieve the Role
                            role = cond['value']
                        if cond['attribute'] == "service":    # Retrieve the Service
                            service = cond['value']
                        elif cond['attribute'] == "resource":   # Retrieve the Resource
                            resource = cond['value']
                        elif cond['attribute'] == "action":   # Retrieve the Action
                            action = cond['value']

                        if(not service or not resource or not action):
                            continue
                        permission = "{0}.{1}.{2}".format(service, resource, action)

                        if len(policy) == 0:
                            policy.append({'role': role, 'permissions': [permission]})

                        else:
                            for r in policy:
                                if r["role"] == role:
                                    if permission not in r["permissions"]:
                                        r["permissions"].append(permission)
    return policy
