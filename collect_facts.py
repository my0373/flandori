#!/usr/bin/env python3
import configparser
import subprocess

class Host(object):
    pass

class Collector(object):
    '''
    This is the collector object. It's entire purpose is to facilitate the collection of facts from hosts.
    '''
    def __init__(self,hostname,config_file,debug=False):
        '''
        The constructor
        :param hostname:
        :param config_file:
        :param debug:
        '''
        self.hostname = hostname
        self.debug = debug
        self.cp = configparser.ConfigParser()
        self.cp.read(config_file)

        ## Read the variables to allow us to collect the variables
        self.cbin = self.cp.get('collector','collector_binary')
        self.inventory = self.cp.get('collector', 'inventory')
        self.fact_store = self.cp.get('collector', 'fact_store')
        self.command = "{cbin} {inventory} -m setup --tree {fact_store}".format(cbin = self.cbin,
                                       inventory = self.inventory,
                                       fact_store = self.fact_store)
        print(self.command)


        print(self.cbin)
        print(self.inventory)

    def collect(self):
        # !/usr/bin/python
        ## get subprocess module



        self.p = subprocess.Popen(self.command, stderr=subprocess.PIPE,stdout=subprocess.PIPE, shell=True)

        ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
        (self.output, self.err) = self.p.communicate()

        ## Wait for date to terminate. Get return returncode ##
        self.p_status = self.p.wait()
        #print("Command output : ", self.output)
        print("Command exit status/return code : ", self.p_status)



if __name__ == '__main__':

    debug = True
    config_file = './conf/flandori.conf'

    c = Collector('localhost',config_file,debug)
    c.collect()

