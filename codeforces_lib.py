#!/bin/env python3

import requests

from codeforces_types import *

class Codeforces(object):
    def __init__(self):
        self.api = constants.url
        self.blog = constants.methods.blog
        self.contest = constants.methods.contest
        self.problemset = constants.methods.problemset

    def _get_method(self, method, payload=None):
        url = self.api + method
        response = requests.get(url, params=payload)
        return response.json()

    def _extract_results(self, json_obj):
        if json_obj["status"] != "OK":
            return []
        return json_obj["result"]
        
    def getBlogComments(self, blogEntryId):
        method = self.blog.comments.format(self.blog.base_str, blogEntryId)
        response = self._get_method(method)
        results = self._extract_results(response)
        commentList = []
        for result in results:
            comment = Comment(result)
            commentList.append(comment)
        return commentList

    def getBlogView(self, blogEntryId):
        method = self.blog.view.format(self.blog.base_str, blogEntryId)
        response = self._get_method(method)
        results = self._extract_results(response)
        blog = Blog()
        blog.from_dict(results)
        return blog
        

    def getHacks(self, contestId):
        method = self.contest.hacks.format(self.contest.base_str, contestId)
        response = self._get_method(method)
        results = self._extract_results(response)
        hacks = []
        for result in results:
            hack = Hack(result)
            hacks.append(hack)
        return hacks
