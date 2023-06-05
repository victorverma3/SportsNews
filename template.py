#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:51:54 2023

@author: victor
"""

# Imports
from scrapers import *

#Data
links = {
    'basketball': 'nba.com',
    'cbasketball': 'espn.com/mens-college-basketball',
    'cfootball': 'espn.com/college-football',
    'cricket': 'espncricinfo.com/cricket-news',
    'football': 'nfl.com',
    'soccer': 'espn.com/soccer'
    }

# Email Templates
def template(sport):
    return '''
        <html>
            <head>
            	<style type="text/css">
            		.body {
            			background-color: #f1f8ff;
            		}
                    .divider {
                        width: 100%;
                    }
                    .feedback {
                        width: 80%;
                        margin: auto;
                        text-align: center;
                        font-size: 2.5vw;
                    }
            		.headlines {
                        text-align: center;
                        font-size: 3vw;
                        padding-bottom: 1%;
            		}
            		.sport {
            			width: 96%;
            			padding: 0% 2% 0% 2%;
            		}
                    .subheader {
                        text-align: center;
                        font-size: 4vw;
                    }
                    /* Adjust font size for MacBook and Desktop */
                    @media (min-width: 769px) {
                        .feedback {
                            width: 80%;
                            margin: auto;
                            text-align: center;
                            font-size: 2vw;
                            padding-bottom: 1%;
                        }
                        .headlines {
                            text-align: center;
                            font-size: 2.5vw;
                            padding-bottom: 1%;
                        }
                        .subheader {
                            text-align: center;
                            font-size: 3.5vw;
                        }
                    }
            	</style>
            </head>
            <body class = "body">
            	<div class = "sport">
                    <h3 class = "subheader" > These are the latest articles on ''' + links[sport] + ''': </h3>
            		<p class = "headlines"> ''' + eval(sport + '()') + ''' </p>
            	</div>
                <hr class = "divider">
                <div class = "feedback" >
                    <p> Submit any feedback, comments, questions, or suggestions through the following form: https://forms.gle/uPGi2kqimA9N2Ejm7 </p>
                </div>
            </body>
        </html>
        '''