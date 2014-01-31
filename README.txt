Purpose
  - package management of configurations needs by JBoss BPMSv6 to leverage mysql/mariadb on Red Hat Enterprise Linux (RHEL) 

Build Procedure
  - ensure that jboss_bpm_soa, bpms, mysql-server and mysql-connector-java RPMs are available (and installed if not using yum)
  - clone this project from github
  - cd /path/to/this/bpms_mysql_rpmbuild
  - rpmbuild --define "_sourcedir `pwd`/SOURCES" -ba SPECS/bpms_mysql.spec
  - rpm -qlp ~/rpmbuild/RPMS/x86_64/bpms_mysql-6.0.0-1.el6.x86_64.rpm
  - sudo rpm -ivh ~/rpmbuild/RPMS/x86_64/bpms_mysql-6.0.0-1.el6.x86_64.rpm
    
  - sudo rpm -e bpms_mysql

 TO-DO
