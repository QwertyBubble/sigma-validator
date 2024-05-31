import logging
import os
import yaml
import datetime

LEVEL = ['informational', 'low', 'medium', 'high', 'critical']
STATUS = ['stable', 'test', 'experimental', 'deprecated', 'unsupported']
REQUIRED = ['title', 'id', 'status', 'description', 'author', 'modified', 'tags', 'logsource', 'detection', 'falsepositives', 'level']

class validator ():
    def required_fields(rule):
        for i in REQUIRED:
            if i not in rule.keys():
                print(f"Title: {rule['title']}; \n", f"\t Attribute {i} must be specified! \n")
        return True

    def check_empty(rule):
        for attr in rule:
            if not rule[attr]:
                print(f"Title: {rule['title']}; \n", f"\t Attribute {attr} must not contain empty value! \n")
        return True

    def title(rule):
        if(int(len(rule['title']) < int(10))):
            print(f"Title: {rule['title']}; \n", "\t Title is too short. Must be greater or equal to 10. \n")
        if(int(len(rule['title']) > int(256))):
            print(f"Title: {rule['title']}; \n", "\t Title is too long. Must be less or equal to 256. \n")
        return True

    def date(rule):
        try:
            datetime.date.fromisoformat(str(rule['modified']))         #for YYYY-MM-DD format
            #datetime.datetime.strptime(rule['modified'], "%Y/%m/%d")    #for YYYY/MM/DD format
        except ValueError:
            print(f"Title: {rule['title']}; \n", "\t Incorrect data format, should be YYYY-MM-DD. \n")
        return True
    
    def status(rule):
        if (rule['status'] not in STATUS):
            print(f"Title: {rule['title']}; \n", f"\t Unknown status: {rule['status']} \n")
        return True
    
    def level(rule):
        if (rule['level'] not in LEVEL):
            print(f"Title: {rule['title']}; \n", f"\t Unknown level: {rule['level']} \n")
        return True
    

def validate(rule):
    validator.required_fields(rule)
    validator.check_empty(rule)
    validator.title(rule)
    validator.date(rule)
    validator.status(rule)
    validator.level(rule)
