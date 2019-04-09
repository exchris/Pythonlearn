#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# all the imports
import os
import sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
