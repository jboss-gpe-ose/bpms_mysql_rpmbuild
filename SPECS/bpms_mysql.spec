Name:           bpms_mysql
Version:        6.0.0
Release:        1%{?dist}
Summary:        JBoss Business Process Management System (BPMS) Deployable for JBoss EAP 6
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        module.xml
Source1:        persistence.xml
Requires:       bpms, mysql-server, mysql-connector-java

%description
Provides configuration required for Red Hat JBoss to connect to an existing MySQL RDBMS.
In particular, will add a mysql "module" to the module path of JBoss EAP and re-configure
the Business Central and Dashbuilder web archives of BPMS6 to us mysql.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers/bpms/com/mysql/jdbc/main
cp %{SOURCE0} $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers/bpms/com/mysql/jdbc/main

mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/standalone/deployments/business-central.war/WEB-INF/classes/META-INF
cp %{SOURCE1} $RPM_BUILD_ROOT/opt/jboss_bpm_soa/jboss-eap-6.1/standalone/deployments/business-central.war/WEB-INF/classes/META-INF/

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s -f -t /opt/jboss_bpm_soa/jboss-eap-6.1/modules/system/layers/bpms/com/mysql/jdbc/main/ /usr/share/java/mysql-connector-java.jar

%files
/opt/jboss_bpm_soa/*
