# winser-stack-1.py
# Authentication
# This program can be used for two or more functionalities:
# a.) user + running-app-of-choice + winser.py [winser-stack-1.py]
#                                             .--param[ip+userid]-(base64)<->auth.py<->.--param[ip-areaid]-(base64) => OK times two
#
# b.) user[1] + running-app-of-choice + winser.py [winser-stack-2.py] .."using-same-LAN"..user[2] + running-app-of-choice + winser.py [winser-stack-2.py]
#                                             .--param[ip+userid[1]]-(base64)<->auth.py<->.--param[ip-userid[2]]-(base64) => OK times two
#                                                                                  ==relay==
#                                             <= OK times two [ip+userid[1]]-(base64)<->auth.py<->.--param[ip-userid[2]]-(base64).--param
#