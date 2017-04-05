# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from kb_maxbin.Utils.MaxBinUtil import MaxBinUtil
#END_HEADER


class kb_maxbin:
    '''
    Module Name:
    kb_maxbin

    Module Description:
    A KBase module: kb_maxbin
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_maxbin.git"
    GIT_COMMIT_HASH = "82afda87e2947bafa572388cb9c6e08ec59b20a0"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_max_bin(self, ctx, params):
        """
        :param params: instance of type "MaxBinInputParams" (required params:
           contig_file: contig file path/shock_id in File structure
           out_header: output file header workspace_name: the name of the
           workspace it gets saved to. semi-required: at least one of the
           following parameters is needed abund_list: contig abundance
           file(s)/shock_id(s) reads_list: reads file(s)/shock_id(s) in fasta
           or fastq format optional params: thread: number of threads;
           default 1 reassembly: specify this option if you want to
           reassemble the bins. note that at least one reads file needs to be
           designated. prob_threshold: minimum probability for EM algorithm;
           default 0.8 markerset: choose between 107 marker genes by default
           or 40 marker genes ref:
           http://downloads.jbei.org/data/microbial_communities/MaxBin/README.
           txt) -> structure: parameter "contig_file" of type "File" (File
           structure for input/output file) -> structure: parameter "path" of
           String, parameter "shock_id" of String, parameter "out_header" of
           String, parameter "workspace_name" of String, parameter
           "abund_list" of list of type "File" (File structure for
           input/output file) -> structure: parameter "path" of String,
           parameter "shock_id" of String, parameter "reads_list" of list of
           type "File" (File structure for input/output file) -> structure:
           parameter "path" of String, parameter "shock_id" of String,
           parameter "thread" of Long, parameter "reassembly" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "prob_threshold" of Double, parameter "markerset" of Long
        :returns: instance of type "MaxBinResult" (result_folder: folder path
           that holds all files generated by run_max_bin report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter "result_folder"
           of String, parameter "obj_ref" of String, parameter "report_name"
           of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_max_bin
        print '--->\nRunning kb_maxbin.run_max_bin\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        maxbin_runner = MaxBinUtil(self.config)
        returnVal = maxbin_runner.run_maxbin(params)

        # reportVal = maxbin_runner.generate_report(returnVal['obj_ref'], params)
        # returnVal.update(reportVal)
        #END run_max_bin

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_max_bin return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
