# -*- coding: utf-8 -*-
"""
SVL 2015-2016
TP poids ideal
Authors: Honore Nintunze, Antonin Durey
"""
from selenium import webdriver

def before_all(context):
    context.navigateur = webdriver.Firefox()
    context.navigateur.get('http://localhost:8080')

def after_all(context):
    context.navigateur.quit()
