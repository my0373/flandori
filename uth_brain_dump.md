Taxonomy of Terms:

SYSTEM - the content management process
ENTITY - a single target that is content managed by SYSTEM
STATE - current verified state of entity (***)
AUDIT - exact record of all state changes made by system
REPO - internal system storage for content to be applied to ENTITIES
TEMPLATE - an initial or target set of STATE for an ENTITY
INHERITED TEMPLATE - templates can be single-parent inherited, i.e. base_rhel->rhel_server->jboss_eap as templates, each inheriting
from its parent. No *multiple* inheritence
ENTITY_GROUP - ENTITIES can be placed into *one* group (i.e. ENTITIES are unique within the system model). 
CLUSTER - CLUSTERS contain ENTITIES and/or ENTITY_GROUPS. They can also contain CLUSTERS (making the CLUSTERS hierarchical). However
ENTITY_GROUP and ENTITY are unique items within the system model.


Highlevel goals:

1: Simplified Content Management
2: State Analysis (target entity - what is your actual state?)
3: Target - RHEL estates and Registries?
4: On-Demand State Analysis - *never* poll machine for state unless we need to change it, i.e, minimal interactions with target
entity

Highlevel wants:

1: Fast
2: Accurate
3: Lightweight
