What content do we need to manage ?

What metadata do we need to retain ?

What sources will we accept content from ?

Where will we deliver content ?

How do we ensure the integrity of the content ?

How can we distribute content in a highly available (and secure) way ?
- idea, maybe a bittorrent like peer to peer content distribution ?
- could blockchain do something cool here ?


How do we version content ?
- crazy idea, possibly use specific container labels for specific content to track specific versions of content to a local provider.
Needs more thought.

How do we present content in many different ways to many different systems ?

How do we enforce (or do we even want to) the metadata captured from the source ?

### Collecting state
One of the primary tasks will be how to collect state information from a target system.

Currently the best tool to collect system state information acrros multiple platforms is Ansible.

Ansible itself is written in Python, and does have a python API, however, it's use by external applications seems to be discouraged, and it's clear it isn't stable enough to depend upon.

However, we know output from the setup module can be dumped as yaml. So using that as the method to pass state information into our model.

#### Possible leads on integration  
Ansible output callback plugins
https://docs.ansible.com/ansible/devel/plugins/callback.html

Specifically around developing these output plugins.
https://docs.ansible.com/ansible/devel/dev_guide/developing_plugins.html

