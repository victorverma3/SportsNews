#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:51:54 2023

@author: victor
"""

# Imports
from scrapers import *

# Data
links = {
    "basketball": "nba.com",
    "cbasketball": "espn.com/mens-college-basketball",
    "cfootball": "espn.com/apis/site/v2/sports/football/college-football/news",
    "cricket": "espncricinfo.com/cricket-news",
    "football": "nfl.com",
    "soccer": "espn.com/soccer",
}


# Email Template
def template(sport):
    return (
        """
        <html>
            <head>
            	<style type="text/css">
                    .divider {
                        width: 100%;
                    }
                    .feedback {
                        width: 80%;
                        margin: auto;
                        text-align: center;
                        font-size: 1.25rem;
                    }
                    .headlines {
                        width: fit-content;
                        margin: auto auto 0.5rem auto;
                        text-align: left;
                        font-size: 2.125rem;
            		}
            		.sport {
            			width: 96%;
            			padding-inline: 2%;
            		}
                    .subheader {
                        text-align: center;
                        font-size: 2.75rem;
                    }
                    @media screen and (max-width: 499px) {
                        .feedback {
                            font-size: 0.625rem;
                        }
                        .headlines {
                            font-size: 0.75rem;
                        }
                        .subheader {
                            font-size: 1.25rem;
                        }
                    }
                    @media screen and (min-width: 500px) and (max-width: 768px) {
                        .feedback {
                            font-size: 0.875rem;
                        }
                        .headlines {
                            font-size: 1.5rem;
                        }
                        .subheader {
                            font-size: 2rem;
                        }
                    }
            	</style>
            </head>
            <body>
            	<div class = "sport">
                    <h3 class = "subheader" > These are the latest articles on """
        + links[sport]
        + """: </h3>
            		<div class = "headlines"> """
        + eval(sport + "()")
        + """ </div>
            	</div>
                <hr class = "divider">
                <div class = "feedback" >
                    <p> Submit any feedback, comments, questions, or suggestions through the following form: https://forms.gle/uPGi2kqimA9N2Ejm7 </p>
                </div>
            </body>
        </html>
        """
    )
