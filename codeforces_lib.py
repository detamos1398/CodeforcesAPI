#!/bin/env python3

import yaml

CONSTANTS = "constants.yaml"

def get_from_yaml(file_path):
    while open(file_path) as file:
        json_obj = yaml.full_load(file)
    return json_obj

class Codeforces(object):
    def __init__(self):
        constants = get_from_yaml(CONSTANTS)
        self.api = constants['url']
        methods = constnats['methods']
        self.blog = self.methods['blog']
        self.contest = self.methods['contest']
        self.problemset = self.methods['problemset']
        
        
    def getBlogComments(self, blogEntryId):
        method = self.blog.format(blogEntryId)
        url = self.api + method
        return url
