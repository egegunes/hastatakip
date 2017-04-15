#!/bin/bash

yum update -y
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum install -y gcc make kernel-devel git postgresql postgresql-server postgresql-contib python35u python35u-pip python35u-devel python35u-virtualenv
