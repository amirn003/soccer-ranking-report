#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pandas as pd
import os, sys
import subprocess as sp
import argparse
import logging
from src import utils as ut
from datetime import datetime, date
from src import generator as gt
import extractSoccerTeam as esoc



def main():

    tmp_dir = 'tmp/'

    usage = "usage: ./PyGenerateReport.py [options] arg"
    parser = argparse.ArgumentParser()


    requiredNamed = parser.add_argument_group('Generate HTML Reports with Jinja')
    requiredNamed.add_argument('-ch', '--contenthtml', help="content html", required=False)
    requiredNamed.add_argument('-hn', '--hostname', help="host name", required=False)
    requiredNamed.add_argument('-o', '--outputpath', help="output path", required=False)
    requiredNamed.add_argument('-cl', '--clean', help="clean-up tmp files", action='store_true', required=False)
    requiredNamed.add_argument("-m", type=str, default="info", help="indicate the level of prints on the terminal (debug, info, error or warning)")
    parser.add_argument("-d", type=str, default="debug", help="indicate the level of prints on log file (debug, info, error or warning)")
    
    
    args = parser.parse_args()

    today = str(date.today())

    log = ("log/")
    directory = os.path.join(log, today)
    log_file_name = "log.txt"
    ut.set_logger(args.m, args.d, directory, log_file_name)

    logger = logging.getLogger('log')

    logger.info("Generate Jinja Report")

    report = "report"
    content = "Premiere_League"
    count = 1

    logger.info(f"Writing Report in : {report}/{content}_report.html")

    sc = esoc.getPremierLeagueRanking()
    logger.info(sc)
    scDf = pd.DataFrame(sc, columns = [ 'Position', 'Team', 'Played', 'Won', 'Drawn', 'Lost', 'Goals For', 'Goals Against', 'Goal Difference', 'Points', 'Form'])
    gt.generateReport(scDf, content, count, today, report)

    report = "report"
    content = "Ligue1"
    count = 2

    logger.info(f"Writing Report in : {report}/{content}_report.html")

    l1r = esoc.getLigue1Ranking()
    logger.info(l1r)
    #l1rDf = pd.DataFrame(l1r, columns = [ 'NA', 'NA', 'Team', 'NA', 'Pts', 'J.', 'G.', 'N.', 'P.', 'p.', 'c.', 'plus', 'G', 'N', 'P'])
    gt.generateReport(l1r, content, count, today, report)


if __name__ == "__main__":
   main()