#!/bin/env python3

import json
import os
import yaml
import requests

from collections import namedtuple

CONSTANTS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'constants.yaml')

def get_from_yaml(file_path):
    with open(file_path) as f:
        json_obj = yaml.full_load(f)
    return json.loads(json.dumps(json_obj), object_hook=lambda d:namedtuple('X', d.keys())(*d.values()))

class Codeforces(object):
    def __init__(self):
        constants = get_from_yaml(CONSTANTS)
        self.api = constants.url
        self.blog = constants.methods.blog
        self.contest = constants.methods.contest
        self.problemset = constants.methods.problemset

    def _get_method(self, method, payload=None):
        url = self.api + method
        response = requests.get(url, params=payload)
        if response.status_code != 200:
            raise 'Failed while getting url ({}) : {}'.format(response.url, response.status_code)
        return response.json()
        
    def getBlogComments(self, blogEntryId):
        method = self.blog.comments.format(self.blog.base_str, blogEntryId)
        return self._get_method(method)

    def getBlogView(self, blogEntryId):
        method = self.blog.view.format(self.blog.base_str, blogEntryId)
        return self._get_method(method)
