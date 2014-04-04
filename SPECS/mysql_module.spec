Name:           mysql_module
Version:        6.0.0
Release:        3%{?dist}
Summary:        JBoss Business Process Management System (BPMS) Deployable for JBoss EAP 6
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        module.xml
Requires:       mysql-server, mysql-connector-java

%description
Provides configuration required for Red Hat JBoss to connect to an existing MySQL RDBMS.
In particular, will add a mysql "module" to the module path of JBoss EAP.


%install
INTEGRATION_HOME=/opt/jboss_bpm_soa
JBOSS_HOME=$RPM_BUILD_ROOT/$INTEGRATION_HOME/jboss-eap-6.1
rm -rf $RPM_BUILD_ROOT
mkdir -p $JBOSS_HOME/modules/system/layers/base/com/mysql/jdbc/main
cp %{SOURCE0} $JBOSS_HOME/modules/system/layers/base/com/mysql/jdbc/main

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s -f -t /opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers/base/com/mysql/jdbc/main/ /usr/share/java/mysql-connector-java.jar

%preun
rm /opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers/base/com/mysql/jdbc/main/mysql-connector-java.jar

%files
/opt/jboss_bpm_soa/*
