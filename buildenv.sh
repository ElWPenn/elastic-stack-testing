#!/bin/bash
#
# @author: Liza Dayoub

# When set, we are running locally not in Jenkins
export AIT_RUN_LOCAL=true

# Build URL
export ES_BUILD_URL=

# Build package extension
export ES_BUILD_PKG_EXT=tar

# Install package 
export AIT_ANSIBLE_PLAYBOOK=get_started/install_xpack

# Setup VM
export AIT_VM=vagrant_vm

# Skip destroying the VM 
export AIT_SKIP_VM_CLEANUP=true

source jenkins_build.sh
