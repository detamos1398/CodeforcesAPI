#!/bin/env python3

import json
import os
import yaml

from collections import namedtuple
from html.parser import HTMLParser
from io import StringIO
from pydoc import locate

def get_obj_from_dict(dic):
    return json.loads(json.dumps(dic), object_hook=lambda d:namedtuple('X', d.keys())(*d.values()))

def get_from_yaml(file_path):
    with open(file_path) as f:
        json_obj = yaml.full_load(f)
    return get_obj_from_dict(json_obj)

CONSTANTS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'constants.yaml')
constants = get_from_yaml(CONSTANTS)

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, data):
        self.text.write(data)

    def get_data(self):
        return self.text.getvalue()


class ReturnObj(object):
    def __init__(self, objtype):
        self.schema = getattr(constants.returnObjSchema, objtype)

    def from_dict(self, json_obj):
        if json_obj is None:
            return
        for key, value in json_obj.items():
            typ = getattr(self.schema, key)
            typ = locate(typ) or locate('codeforces_types.{}'.format(typ))
            setattr(self, key, typ(value))

    def pretty_print(self):
        ret_str = ''
        for key, value in vars(self).items():
            if key != 'schema' and value is not None:
                if __name__ != type(value).__module__:
                    htmlStripper = MLStripper()
                    htmlStripper.feed(str(value))
                    ret_str += ('{}:\t{}\n'.format(key, htmlStripper.get_data()))
                else:
                    ret_str += '{}:\n'.format(key) + value.pretty_print()
        return ret_str


class Blog(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'blog')
        self.from_dict(json_obj)


class Comment(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'comment')
        self.from_dict(json_obj)


class Party(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'party')
        self.from_dict(json_obj)

class Hack(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'hack')
        self.from_dict(json_obj)        
        
class Member(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'member')
        self.from_dict(json_obj)

class Problem(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'problem')
        self.from_dict(json_obj)

class JudgeProtocol(ReturnObj):
    def __init__(self, json_obj=None):
        ReturnObj.__init__(self, 'judgeprotocol')
        self.from_dict(json_obj)
