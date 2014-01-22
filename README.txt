Purpose
  - package management of JBoss Business Process Management (BPMS) v6 on Red Hat Enterprise Linux (RHEL)

Build Procedure
  - ensure that jboss_bpm_soa, bpms, mysql-server and mysql-connector-java RPMs are available (and installed if not using yum)
  - clone this project from github
  - cd /path/to/this/bpms_rpmbuild
  - rpmbuild --define "_sourcedir `pwd`/SOURCES" -ba SPECS/bpms_mysql.spec
  - rpm -qlp ~/rpmbuild/RPMS/x86_64/bpms-6.0.0-1.el6.x86_64.rpm
  - sudo rpm -ivh --replacefiles ~/rpmbuild/RPMS/x86_64/bpms-6.0.0-1.el6.x86_64.rpm
    - NOTE:  
        - BPMS6 intentionally over-rides several configuration files from JBoss EAP6.1.1
        - writing over these files is safe and can be done with RPM via "--replacefiles" flag
    
  - sudo rpm -e bpms

 TO-DO
