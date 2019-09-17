from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

# load dataset
fatalities = pd.read_csv('./data')