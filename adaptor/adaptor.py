import json

from adaptor import gcloud_parser
from adaptor import semantic_parser

def policy2dnf(policy, tenant, apf):
    return gcloud_parser.policy2dnf(policy)


def policy2local(dnf_policy):
    return semantic_parser.policy2local(dnf_policy)
