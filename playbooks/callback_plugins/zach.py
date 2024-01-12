# (c) 2012-2014, Ansible, Inc
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: tree
    type: notification
    requirements:
      - invoked in the command line
    short_description: Save host events to files
    version_added: "2.0"
    options:
        directory:
            version_added: '2.11'
            description: directory that will contain the per host JSON files. Also set by the C(--tree) option when using adhoc.
            ini:
                - section: callback_tree
                  key: directory
            env:
                - name: ANSIBLE_CALLBACK_TREE_DIR
            default: "~/.ansible/tree"
            type: path
    description:
        - "This callback is used by the Ansible (adhoc) command line option C(-t|--tree)."
        - This produces a JSON dump of events in a directory, a file for each host, the directory used MUST be passed as a command line option.
'''
from ansible.playbook.task import Task
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.callback import CallbackBase
from ansible.utils.path import makedirs_safe, unfrackpath
from ansible.vars.manager import VarsWithSources

ORIGINAL_ACCESSOR = VarsWithSources.__getitem__

class CallbackModule(CallbackBase):
    '''
    This callback prints the source of variables
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'zach'
    CALLBACK_NEEDS_ENABLED = True
    RECORDS = {}

    def v2_runner_on_start(self, host, task):
        self.RECORDS[host] = self.RECORDS.get('host', {"tasks": {}})
        if task._variable_manager:
            vars = task._variable_manager.get_vars(task.get_play(), host, task)
            self.RECORDS[host]['tasks'][task._uuid] = TaskData(task, vars)

    def v2_runner_on_ok(self, result):
        print(self.RECORDS)
    
class TaskData():
    def __init__(self, task: Task, vars: VarsWithSources):
        self.uuid = task._uuid
        self.data = task.serialize()
        self.sources = vars.sources

    def __repr__(self) -> str:
        return str({
            "uuid": self.uuid,
            "data": self.data.keys(),
            "sources": len(self.sources)
        })